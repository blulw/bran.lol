document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("autoplay-fix");
    console.log(button)
    button.onclick = () => {
        var number = Math.floor(Math.random() * 9);

    if (number == 0) {
        var audio = new Audio("!sick.mp3");
        var text = new String("sick - glaive")
    } 
    else if (number == 1) {
        var audio = new Audio("!BHSS03NOVAGOONNMNS - RED.mp3");
        var text = new String("RED - BHSS03NOVAGOONNMNS")
    }
    else if (number == 2) {
        var audio = new Audio("!chanelfather - 1tap.mp3");
        var text = new String("1tap - chanelfather")
    }
    else if (number == 3) {
        var audio = new Audio("!coke_blow.mp3");
        var text = new String("coke//blow - glaive")
    }
    else if (number == 4) {
        var audio = new Audio("!hissiest - wrong (prod. SweetBoobs).mp3");
        var text = new String("wrong - hissiest")
    }
    else if (number == 5) {
        var audio = new Audio("!d0llywood1 - he's just like me (prod. wastedyouth)");
        var text = new String("he's just like me - d0llywood1")
    }
    else if (number == 6) {
        var audio = new Audio("!findhelp.mp3");
        var text = new String("findhelp - lieu")
    }
    else if (number == 7) {
        var audio = new Audio("!life is pain.mp3");
        var text = new String("life is pain - glaive")
    }
    else if (number == 8) {
        var audio = new Audio("!loose ties.mp3");
        var text = new String("loose ties - ericdoa")
    }
    document.getElementById("current-song").innerHTML = text;
    audio.play();
        button.style.display = 'none';
    }
})
