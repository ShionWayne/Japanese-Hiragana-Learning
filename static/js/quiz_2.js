var user_answer = []

function set_hiragana_draggable(){
    $(".quiz_2_source-box").draggable({cursor: "move", revert: "invalid"})
}

function build_drag_zone(content){
    $("#quiz_2_content").empty()
    for (i=0; i < content.data.length; i++){
        let line = $("<div>").addClass("quiz-2-row")
        line.addClass("row")
        line.attr("id", "quiz2_line"+i.toString())
        let left_block = $("<div>").addClass("col-sm-6")
        let hiragana = $("<div>").addClass("quiz_2_source-box")
        hiragana.text(content.data[i].hiragana)
        hiragana.attr("h", content.data[i].hiragana)
        left_block.append(hiragana)
        line.append(left_block)
        let right_block = $("<div>").addClass("col-sm-6")
        let romanization = $("<div>").addClass("quiz_2_target-box")
        romanization.attr("r", content.data[i].roman)
        romanization.text("Block "+i.toString())
        let audio = $("<audio>")
        audio.attr("src", content.data[i].audio)
        audio.attr("controls", "controls")
        right_block.append(romanization)
        right_block.append(audio)
        line.append(right_block)
        $("#quiz_2_content").append(line)
    }
    set_hiragana_draggable()
    set_romaization_droppable()
}

function set_romaization_droppable(){
    $(".quiz_2_target-box").droppable({
        accept: ".quiz_2_source-box",
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
    $("#quiz_2_result_zone").empty()
    $("#quiz_2_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great!")
    right.addClass("result_word")
    $("#quiz_2_result_zone").append(right)
    let next_button = $("<button>")
    next_button.attr("id", "next_button_correct")
    next_button.addClass("btn btn-primary mb-2")
    next_button.text("Next")
    $("#quiz_2_result_zone").append(next_button)
}

function generate_red_zone(){
    $("#quiz_2_result_zone").empty()
    $("#quiz_2_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz_2_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz_2_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        build_drag_zone(content)
        $("#quiz_2_result_zone").removeClass("red_zone")
        $("#quiz_2_result_zone").empty()
        user_answer = []
    })
}

$(document).ready(function (){
    build_drag_zone(content)
    $(".quiz2_submit").click(function (){
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