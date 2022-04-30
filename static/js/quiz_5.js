function reset_question(data_l){
    for(let i=1; i < data_l+1; i++){
        $("#Radio"+i.toString())[0].checked = false;
    }
}

function generate_green_zone(){
    $("#quiz5_result_zone").empty()
    $("#quiz5_result_zone").addClass("green_zone")
    let right = $("<span>").text("Great!")
    right.addClass("result_word")
    $("#quiz5_result_zone").append(right)
    let next_button = $("<button>")
    next_button.attr("id", "next_button_correct")
    next_button.addClass("btn btn-primary mb-2")
    next_button.text("Next")
    $("#quiz5_result_zone").append(next_button)
}

function generate_red_zone(w3){
    $("#quiz5_result_zone").empty()
    $("#quiz5_result_zone").addClass("red_zone")
    let wrong = $("<span>").text("Wrong answer!")
    wrong.addClass("result_word")
    $("#quiz5_result_zone").append(wrong)
    let try_again = $("<button>")
    try_again.attr("id", "try_again_button")
    try_again.text("Try Again!")
    $("#quiz5_result_zone").append(try_again)
    $("#try_again_button").click(function (){
        reset_question(data_l);
        $("#quiz5_result_zone").removeClass("red_zone")
        $("#quiz5_result_zone").empty()
        alert(w3)
    })
}

$(document).ready(function(){
    // trigger button click for validation
    $("#quiz_5_submit").click(function(){
        var select_val = 0;
        // iterate all #Radio<Int> to check which one is checked
        for(let i=1; i < data_l+1; i++){
            if($("#Radio"+i.toString())[0].checked){
                // get the selected value
                select_val = $("#Radio"+i.toString())[0].value;
            }
        }
        let pid = data.q_id;
        // use ajax to post: q_id, selected_val
        $.ajax({
            type: "POST",
            url: "/quiz_valid/" + pid,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(select_val),
            success: function(result){
                console.log(result);
                let validtion = result["validation"];
                console.log(validtion);
                if (validtion == true){
                    // show next page and correct alert
                    generate_green_zone();
                    if(pid != qnum-1){
                        $("#next_button_correct").click(function(){
                            window.location.href = '/quiz/' + (pid+1).toString();
                        });
                    }else{
                        $("#next_button_correct").click(function(){
                            window.location.href = '/quiz_end';
                        });
                    }
                }else{
                    // show error page and reset everything
                    generate_red_zone("haha");
                }

            },
            error: function(request, status, error){
                console.log("Quiz5 Ajax Error");
            }
        })
    })
})
