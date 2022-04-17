$(function() {
    $("#check").click(function(){
        $("#check_answer").empty()
        if($("#input").val() == "no") {
            $("#check_answer").append("<p>Wonderful! This word means 'no'</p>")
            $("#check_answer").append("<button type='submit' id='correct'>Finish</button>")
            $("#correct").click(function(){
                window.location.href = '/quiz_end'
            })
            
        } else {
            $("#check_answer").append("<p>Wrong answer!</p>")
            $("#check_answer").append("<button type='submit' id='wrong'>Try Again</button>")
            $("#wrong").click(function(){
                $("#input").val('')
                $("#check_answer").empty()
            })
        }
    })
})