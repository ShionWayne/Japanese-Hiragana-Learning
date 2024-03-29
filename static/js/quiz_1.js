var user_answer = []

function set_hiragana_draggable(){
    $(".quiz1_hiragana").draggable({cursor: "move", revert: "invalid"})
}

var target_list = []
var source_list = []

function randomsort(a, b) {
    return Math.random()>.5 ? -1 : 1;
}

function build_random_list() {
    for (i=0; i < content.problem_and_answer.length; i++){
        target_list.push({"roman": content.problem_and_answer[i].Romanization, "eng": content.problem_and_answer[i].English})
        source_list.push(content.problem_and_answer[i].hiragana)
    }
    target_list.sort(randomsort)
    source_list.sort(randomsort)
}

function build_drag_zone(content){
    $("#quiz1_drag_zone").empty()
    for (i=0; i < content.problem_and_answer.length; i++){
        let line = $("<div>").addClass("drag_grid")
        line.attr("id", "quiz1_line"+i.toString())
        let left_block = $("<div>").addClass("help_div")
        let hiragana = $("<div>").addClass("quiz1_hiragana")
        hiragana.text(source_list[i])
        hiragana.attr("h", source_list[i])
        left_block.append(hiragana)
        line.append(left_block)
        let middle_block = $("<div>").addClass("help_div")
        line.append(middle_block)
        let right_block = $("<div>").addClass("help_div")
        let romanization = $("<div>").addClass("quiz1_Romanization")
        romanization.text(target_list[i].roman)
        romanization.attr("r", target_list[i].roman)
        right_block.append(romanization)
        let eng = $("<div>").addClass("english")
        eng.text(target_list[i].eng)
        right_block.append(eng)
        line.append(right_block)
        $("#quiz1_drag_zone").append(line)
    }
    set_hiragana_draggable()
    set_romaization_droppable()
    $(".english").hide()
    $(".quiz1_submit").removeAttr("disabled")
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
            $.each($(".quiz1_hiragana"), function (){
                let h = $(this).attr("h")
                if (h == answer_h){
                    $(this).draggable({disabled: "true"})
                }
            })
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
    // next_button.addClass("btn btn-primary mb-2")
    next_button.text("Next")
    $("#quiz1_result_zone").append(next_button)
    $(".quiz1_submit").attr('disabled',"true")
}

function generate_red_zone(w3){
    $("#quiz1_result_zone").empty()
    $("#quiz1_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz1_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz1_result_zone").append(try_again)
    $(".quiz1_submit").attr('disabled',"true")
    $("#try_again_button").click(function (){
        build_drag_zone(content)
        $("#quiz1_result_zone").removeClass("red_zone")
        $("#quiz1_result_zone").empty()
        user_answer = []
        alert(w3)
    })
}

$(document).ready(function (){
    build_random_list()
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
                let w3 = result["wrong3"]
                console.log("w3=" + w3)
                console.log(res)
                console.log(res.correct === "True")
                if (res.correct === "True"){
                    generate_green_zone()
                    $(".english").show()
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
                    generate_red_zone(w3)
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