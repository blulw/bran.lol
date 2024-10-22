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
                audio = new Audio("https://www.dropbox.com/scl/fi/j8qix48xrm3wva6omeccb/sick.mp3?rlkey=s6dytwpzcdmbgst8rlnvllqnf&st=2mv93s7f&dl=1");
                text = "sick - glaive";
                break;
            case 1:
                audio = new Audio("https://www.dropbox.com/scl/fi/zdd7bwfc4366h4wnlyasj/BHSS03NOVAGOONNMNS-RED.mp3?rlkey=nzmw7soaab6qs7f2aghg1mk48&st=uzmkbqs5&dl=1");
                text = "RED - BHSS03NOVAGOONNMNS";
                break;
            case 2:
                audio = new Audio("https://www.dropbox.com/scl/fi/3jdbrvokyxm90racepx68/chanelfather-1tap.mp3?rlkey=owpcz7jpepgpfcafuqn8dbo5j&st=nq9rgrmz&dl=1");
                text = "1tap - chanelfather";
                break;
            case 3:
                audio = new Audio("https://www.dropbox.com/scl/fi/q20fysysqr6ryc4zsgqsx/coke_blow.mp3?rlkey=eiptnu6utz1fqvfbtq1r22a86&st=wlf6zlz3&dl=1");
                text = "coke//blow - glaive";
                break;
            case 4:
                audio = new Audio("https://www.dropbox.com/scl/fi/hcmilz126hb4ndlxf7v01/hissiest-wrong-prod.-SweetBoobs.mp3?rlkey=05bcp4tg21qi4nziz7wja6z65&st=4ja9frkn&dl=1");
                text = "wrong - hissiest";
                break;
            case 5:
                audio = new Audio("https://www.dropbox.com/scl/fi/w4fmk6h23msczd2jtx9hn/d0llywood1-he-s-just-like-me-prod.-wastedyouth.mp3?rlkey=oe6wv9bjaeifhqniqtblmq9l3&st=x2wgyssj&dl=1");
                text = "he's just like me - d0llywood1";
                break;
            case 6:
                audio = new Audio("https://www.dropbox.com/scl/fi/fhiz7zxbjjt5uh495mp7u/findhelp.mp3?rlkey=9aah1rp5wfx6h9btow4d0fdqj&st=sj7swurv&dl=1");
                text = "findhelp - lieu";
                break;
            case 7:
                audio = new Audio("https://www.dropbox.com/scl/fi/mnqg0pisuikpez60r55uc/life-is-pain.mp3?rlkey=yjwraillk3prpxg7libybjsyu&st=fy5qxe5z&dl=1");
                text = "life is pain - glaive";
                break;
            case 8:
                audio = new Audio("https://www.dropbox.com/scl/fi/t1ij3f5afqt8pvs7mcgkd/loose-ties.mp3?rlkey=eejd7yvtgc88u421uktbwkc0x&st=w2o8xmuz&dl=1");
                text = "loose ties - ericdoa";
                break;
        }


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
