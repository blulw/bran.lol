document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("autoplay-fix");
    const songbutton = document.getElementById("song-buttons");
    let audio = null;
    let mute = false;

    button.onclick = () => {
        const number = Math.floor(Math.random() * 9);
        let text;


        switch (number) {
            case 0:
                audio = new Audio("https://media.bran.lol/music/sick.mp3");
                text = "sick - glaive";
                break;
            case 1:
                audio = new Audio("https://media.bran.lol/music/RED.mp3");
                text = "RED - BHSS03NOVAGOONNMNS";
                break;
            case 2:
                audio = new Audio("https://media.bran.lol/music/1tap.mp3");
                text = "1tap - chanelfather";
                break;
            case 3:
                audio = new Audio("https://media.bran.lol/music/coke.mp3");
                text = "coke//blow - glaive";
                break;
            case 4:
                audio = new Audio("https://media.bran.lol/music/wrong.mp3");
                text = "wrong - hissiest";
                break;
            case 5:
                audio = new Audio("https://media.bran.lol/music/justlikeme.mp3");
                text = "he's just like me - d0llywood1";
                break;
            case 6:
                audio = new Audio("https://media.bran.lol/music/findhelp.mp3");
                text = "findhelp - lieu";
                break;
            case 7:
                audio = new Audio("https://media.bran.lol/music/pain.mp3");
                text = "life is pain - glaive";
                break;
            case 8:
                audio = new Audio("https://media.bran.lol/music/loose.mp3");
                text = "loose ties - ericdoa";
                break;
        }

        audio.loop = true;

        document.getElementById("current-song").innerHTML = text;
        audio.play();
        button.style.display = 'none';
    };

    songbutton.onclick = () => {
        if (audio) {
            mute = !mute;
            if (mute) {
                songbutton.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-music-off">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                        <path d="M6 17m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0" />
                        <path d="M14.42 14.45a3 3 0 1 0 4.138 4.119" />
                        <path d="M9 17v-8m0 -4v-1h10v11" />
                        <path d="M12 8h7" />
                        <path d="M3 3l18 18" />
                    </svg>
                `;
                audio.volume = 0;
            } else {
                songbutton.innerHTML = `
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-music">
                        <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                        <path d="M3 17a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />
                        <path d="M13 17a3 3 0 1 0 6 0a3 3 0 0 0 -6 0" />
                        <path d="M9 17v-13h10v13" />
                        <path d="M9 8h10" />
                    </svg>
                `;
                audio.volume = 1;
            }
        }
    };
});
