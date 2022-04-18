
function playMusic(){
    // console.log(file_url);
    var music = new Audio();
    music.play();
}

$(document).ready(function(){
    let audio = $("<audio>");
    audio.attr("src", content.audio);
})

// C:\Users\Gilbert\Desktop\Japanese-Hiragana-Learning\static\audio\quiz\2\au.mp3