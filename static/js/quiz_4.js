function generate_green_zone(){
    $("#quiz_4_result_zone").empty()
    $("#quiz_4_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great! This word means " + data.eng)
    right.addClass("result_word")

    $("#quiz_4_result_zone").append(right)
    let next_button = $("<button>")
    next_button.attr("id", "next_button_correct")
    next_button.text("Next")
    $("#quiz_4_result_zone").append(next_button)
}

function generate_red_zone(w3){
    $("#quiz_4_result_zone").empty()
    $("#quiz_4_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    // wrong.addClass("result_word")
    $("#quiz_4_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz_4_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        $("#quiz_4_button").prop('disabled', false);
        $("#quiz_4_input").prop('disabled', false);
        $("#quiz_4_input").focus()
        $("#quiz_4_result_zone").removeClass("red_zone")
        $("#quiz_4_result_zone").empty()
        alert(w3)
    })
}

$(document).ready(function () {
    $("#quiz_4_button").click(function (){
        console.log("data type:" + data.q_type)
        $(this).prop('disabled', true);
        $("#quiz_4_input").prop('disabled', true);
        console.log("new version")
        let time = new Date()
        let answer_value = $("#quiz_4_input").val()
        console.log("input+"+answer_value)
        let answer = {
            "id": pid,
            "q_type": data.q_type,
            "eng": data.eng,
            "time": time,
            "user_answer": answer_value
        }
        $.ajax({
            type: "POST",
            url: "/quiz_valid/" + pid,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(answer),
            success: function(result){
                let res = result["newrecord"]
                let w3 = result["wrong3"]
                console.log("w3=" + w3)
                console.log(pid);
                console.log(res)
                console.log(res.correct === "True")
                if (res.correct === "True"){
                    generate_green_zone()
                    if(pid != qnum-1){
                        $("#next_button_correct").click(function(){
                            console.log("here")
                            window.location.href = '/quiz/' + (pid+1).toString();
                        });
                    }else{
                        $("#next_button_correct").click(function(){
                            console.log("end")
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