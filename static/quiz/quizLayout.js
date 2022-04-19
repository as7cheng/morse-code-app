$(document).ready(function(){
    if(data && data.img && data.img.length !== 0) {
        $("#quizLeftBox").html(`<img src="${data.img}" alt="quizImg">`);
    } else {
        $("#quizLeftBox").html(`
            <audio controls>
                <source src="${data.audio}" type="audio/ogg">
                <source src="${data.audio}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
        `)
    }

    if(data && data.img2 && data.img2.length !== 0) {
        $("#quizRightBox").html(`<img src="${data.img2}" alt="quizImg">`);
    } else {
        $("#quizRightBox").html(`<i class="fas fa-solid fa-question"></i>`)
    }
})