document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("autoplay-fix");
    console.log(button)
    button.onclick = () => {
        var number = Math.floor(Math.random() * 9);

    if (number == 0) {
        var audio = new Audio("Flovry x tender spring - backpack City.mp3");
        var text = new String("Flovry x tender spring - Backpack City")
    } 
    else if (number == 1) {
        var audio = new Audio("Sorry for Not Answering the Phone I'm Too Busy Trying to Fly Away.mp3");
        var text = new String("In Love With a Ghost - Sorry for Not Answering the Phone I'm Too Busy Trying to Fly Away")
    }
    else if (number == 2) {
        var audio = new Audio("my heart flutters when i see you.mp3");
        var text = new String("Biosphere - my heart flutters when i see you")
    }
    else if (number == 3) {
        var audio = new Audio("Je T’aime.mp3");
        var text = new String("Sugi.wa - Je T’aime")
    }
    else if (number == 4) {
        var audio = new Audio("it's finally raining again.mp3");
        var text = new String("Elijah Who - it's finally raining again")
    }
    else if (number == 5) {
        var audio = new Audio("I Fell in Love with You One Night in September.mp3");
        var text = new String("Rook1e - I Fell in Love with You One Night in September")
    }
    else if (number == 6) {
        var audio = new Audio("haiku.mp3");
        var text = new String("Nohidea - haiku")
    }
    else if (number == 7) {
        var audio = new Audio("falling asleep at 3_37am.mp3");
        var text = new String("idealism - falling asleep at 3:37am")
    }
    else if (number == 8) {
        var audio = new Audio("coffee on the beach..mp3");
        var text = new String("halberd - coffee on the beach.")
    }
    document.getElementById("current-song").innerHTML = text;
    audio.play();
        button.style.display = 'none';
    }
})
