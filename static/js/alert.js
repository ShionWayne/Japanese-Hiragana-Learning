function alert(wrong_num){
    // wrong_num == 1 means it has 3 consecutive wrong tries
    if (wrong_num == 1) {
        $("#content").empty()

        let warn = $("<div>").text("You may want to stop here and learn again. ")
        warn.addClass("warn")
        $("#content").append(warn)

        let relearn = $("<button>")
        relearn.attr("id", "relearn")
        relearn.addClass("relearn")
        relearn.text("Re-Learn")
        $("#content").append(relearn)

        $("#relearn").click(function(){
            window.location.href = '/startlearning'
        })

        let cont = $("<a>")
        let current_url = window.location.href
        cont.attr("href", current_url)
        cont.addClass("cont")
        cont.text("Continue Testing")
        $("#content").append(cont)
    }
}