var user_answer = []

function set_hiragana_draggable(){
    $(".quiz1_hiragana").draggable({cursor: "move", revert: "invalid"})
}

function build_drag_zone(content){
    $("#quiz1_drag_zone").empty()
    for (i=0; i < content.problem_and_answer.length; i++){
        let line = $("<div>").addClass("drag_grid")
        line.attr("id", "quiz1_line"+i.toString())
        let left_block = $("<div>").addClass("help_div")
        let hiragana = $("<div>").addClass("quiz1_hiragana")
        hiragana.text(content.problem_and_answer[i].hiragana)
        hiragana.attr("h", content.problem_and_answer[i].hiragana)
        left_block.append(hiragana)
        line.append(left_block)
        let middle_block = $("<div>").addClass("help_div")
        line.append(middle_block)
        let right_block = $("<div>").addClass("help_div")
        let romanization = $("<div>").addClass("quiz1_Romanization")
        romanization.text(content.problem_and_answer[i].Romanization)
        romanization.attr("r", content.problem_and_answer[i].Romanization)
        right_block.append(romanization)
        line.append(right_block)
        $("#quiz1_drag_zone").append(line)
    }
    set_hiragana_draggable()
    set_romaization_droppable()
}

function set_romaization_droppable(){
    $(".quiz1_Romanization").droppable({
        accept: ".quiz1_hiragana",
        drop: function (event, ui){
            let answer_h = ui.draggable.attr("h")
            let answer_r = $(this).attr("r")
            let answer = {"hiragana": answer_h, "Romanization": answer_r}
            user_answer.push(answer)
            console.log(user_answer)
            $(this).droppable({disabled: true})
        }
    })
}

function generate_green_zone(){
    $("#quiz1_result_zone").empty()
    $("#quiz1_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great!")
    right.addClass("result_word")
    $("#quiz1_result_zone").append(right)
    let next_button = $("<button>")
    next_button.attr("id", "next_button_correct")
    next_button.addClass("btn btn-primary mb-2")
    next_button.text("Next")
    $("#quiz1_result_zone").append(next_button)
}

function generate_red_zone(){
    $("#quiz1_result_zone").empty()
    $("#quiz1_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz1_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz1_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        build_drag_zone(content)
        $("#quiz1_result_zone").removeClass("red_zone")
        $("#quiz1_result_zone").empty()
        user_answer = []
    })
}

$(document).ready(function (){
    $("#quiz1_problem_zone").text(content.problem_text)
    build_drag_zone(content)
    $(".quiz1_submit").click(function (){
        let time = new Date()
        let record = {
            "id": pid,
            "q_type": content.q_type,
            "time": time,
            "user_answer":user_answer
        }
        $.ajax({
            type: "POST",
            url: "/quiz_valid/"+pid,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(record),
            success: function (result){
                let res = result["newrecord"]

                console.log(res)
                console.log(res.correct === "True")
                if (res.correct === "True"){
                    generate_green_zone()
                    if(pid != qnum-1){
                        $("#next_button_correct").click(function(){
                            window.location.href = '/quiz/' + (pid+1).toString();
                        });
                    }else{
                        $("#next_button_correct").click(function(){
                            window.location.href = '/quiz_end';
                        });
                    }
                } else {
                    generate_red_zone()
                }
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
        })
})