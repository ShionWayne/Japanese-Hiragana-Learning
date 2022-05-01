$(document).ready(function (){
    let stroke = $("<img>")
    stroke.attr("src", content.stroke)
    stroke.attr("width", "100%")
    $(".hiragana_learn").append(stroke)
    let line1 = $("<div>")
    line1.attr("class", "row")
    line1.text("The Romanization of this hiragana is "+"'"+content.id+"'.")
    let line2 = $("<div>")
    line2.attr("class", "row")
    line2.text("It sounds like "+"'"+content.sounds_like+"'"+" in English.")
    let line3 = $("<div>")
    line3.attr("class", "row")
    let line3_txt = $("<span>")
    line3_txt.text("Play sound: ")
    line3.append(line3_txt)
    let audio = $("<audio>")
    audio.attr("src", content.audio)
    audio.attr("controls", "controls")
    line3.append(audio)
    $(".text_learn").append(line1)
    $(".text_learn").append("<br>")
    $(".text_learn").append(line2)
    $(".text_learn").append("<br>")
    $(".text_learn").append(line3)
    
    $(".got_it_learn").click(function(){
        window.location.href = "../startlearning"
    })
    // let prev_a = $("<a>")
    // prev_a.text("Prev")
    // if (content.prev == "None"){
    //     prev_a.attr('href', '/startlearning')
    // } else {
    //     prev_a.attr('href', '/learn/'+content.prev)
    // }
    // $(".prev_learn").append(prev_a)

    // let next_a = $("<a>")
    // let gotit = $("<a>")
    // gotit.text("I Got It!")
    // gotit.attr("href", "/startlearning")
    // next_a.text("Next")
    // if (content.next == "None"){
    //     next_a.attr('href', '/quiz/0')
    //     gotit.attr('href', '/quiz/0')
    // } else {
    //     next_a.attr('href', '/learn/'+content.next)
    //     gotit.attr('href', '/learn/'+content.next)
    // }
    // $(".next_learn").append(next_a)
    // $(".got_it_learn").append(gotit)
})