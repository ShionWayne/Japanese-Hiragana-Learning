function generate_green_zone(){
    $("#quiz_3_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great!")
    right.addClass("result_word")
    $("#quiz_3_result_zone").append(right)
    let next_button = $("<button>")
    next_button.append($("<a>").attr("href", "/quiz/4").text("Next"))
    $("#quiz_3_result_zone").append(next_button)
}

function generate_red_zone(){
    $("#quiz_3_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz_3_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz_3_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        $("#quiz_3_input").focus()
        $("#quiz_3_result_zone").removeClass("red_zone")
        $("#quiz_3_result_zone").empty()
    })
}

$(document).ready(function () {
    $("#quiz_3_button").click(function (){
        let time = new Date()
        let answer_value = $("#quiz_3_input").val()
        let answer = {
            "id": "3",
            "time": time,
            "user_answer": answer_value
        }
        $.ajax({
            type: "POST",
            url: "/quiz/3",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(answer),
            success: function (result){
                let res = result["newrecord"]

                console.log(res)
                console.log(res.correct === "True")
                if (res.correct === "True"){
                    generate_green_zone()
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