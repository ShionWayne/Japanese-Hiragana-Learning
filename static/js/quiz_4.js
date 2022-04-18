$(function() {
    $("#previous").click(function(){
        window.location.href = '/quiz/3'
    });
    $("#next").click(function(){
        window.location.href = '/quiz_end'
    });
    $("#check").click(function(){
        $("#check_answer").empty()
        if($("#input").val().toLowerCase() == data[0]["roman"]) {
            $("#check_answer").addClass("green_zone")
            let correct = $("<span>").text("Great!")
            $("#check_answer").append(correct)
            let next_button = $("<button>Finish</button>")
            next_button.attr("id", "go_to_next")
            $("#check_answer").append(next_button)
            $("#go_to_next").click(function(){
                window.location.href = '/quiz_end'
            })
            
        } else {
            $("#check_answer").addClass("red_zone")
            let wrong = $("<span>").text("Wrong answer!")
            $("#check_answer").append(wrong)
            let try_again = $("<button>Try Again</button>")
            try_again.attr("id", "try_again_button")
            $("#check_answer").append(try_again)
            $("#try_again_button").click(function(){
                $("#input").val('')
                $("#check_answer").empty()
                $("#check_answer").removeClass("red_zone green zone")
            })
        }
    })
})