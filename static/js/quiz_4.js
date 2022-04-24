// $(function() {
//     $("#previous").click(function(){
//         window.location.href = '/quiz/3'
//     });
//     $("#next").click(function(){
//         window.location.href = '/quiz_end'
//     });
//     $("#check").click(function(){
//         $("#check_answer").empty()
//         if($("#input").val().toLowerCase() == data[0]["roman"]) {
//             $("#check_answer").addClass("green_zone")
//             let correct = $("<span>").text("Great!")
//             $("#check_answer").append(correct)
//             let next_button = $("<button>Finish</button>")
//             next_button.attr("id", "go_to_next")
//             $("#check_answer").append(next_button)
//             $("#go_to_next").click(function(){
//                 window.location.href = '/quiz_end'
//             })
            
//         } else {
//             $("#check_answer").addClass("red_zone")
//             let wrong = $("<span>").text("Wrong answer!")
//             $("#check_answer").append(wrong)
//             let try_again = $("<button>Try Again</button>")
//             try_again.attr("id", "try_again_button")
//             $("#check_answer").append(try_again)
//             $("#try_again_button").click(function(){
//                 $("#input").val('')
//                 $("#check_answer").empty()
//                 $("#check_answer").removeClass("red_zone green zone")
//             })
//         }
//     })
// })

function generate_green_zone(){
    $("#quiz_4_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great!")
    right.addClass("result_word")
    $("#quiz_4_result_zone").append(right)
    let next_button = $("<button>")
    next_button.append($("<a>").attr("href", "/quiz_end").text("Next"))
    $("#quiz_4_result_zone").append(next_button)
}

function generate_red_zone(){
    $("#quiz_4_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz_4_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz_4_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        $("#quiz_4_input").focus()
        $("#quiz_4_result_zone").removeClass("red_zone")
        $("#quiz_4_result_zone").empty()
    })
}

$(document).ready(function () {
    $("#quiz_4_button").click(function (){
        console.log("data type:" + data.q_type)
        let time = new Date()
        let answer_value = $("#quiz_4_input").val()
        let answer = {
            "id": pid,
            "q_type": data.q_type,
            "time": time,
            "user_answer": answer_value
        }
        $.ajax({
            type: "POST",
            url: "/quiz_valid/" + pid,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(answer),
            success: function (result){
                let res = result["newrecord"]
                console.log(pid);
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