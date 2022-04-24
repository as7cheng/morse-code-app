function letter_menu(data){
    var result = $("<div class='mid'></div>");
    var target_letter = letter["letter"];

    data.forEach((item, index) => {
        if(item["letter"] == target_letter){
            letter_in = $("<u class='pad2 color3'>" + item["letter"] + "</u>");
            result.append(letter_in);
        }
        else{
            letter_in = $("<a class='pad2 color2' href='/letters/"+item["id"]+"'>" + item["letter"] + "</a>");
            result.append(letter_in);
        }
    })
    $("#menu").append(result)
}

function next_button(){
    var result = $("<div class='letterBottomBtn'></div>");
    var num = letter["id"];
    if(num < 10){
        var btn = $("<button type='button' class='btn btn-warning letterNextBtn' id='letterNextBtn'>Next</button>");
        result.append(btn)
    }
    else{
        var btn = $("<button type='button' class='btn btn-warning letterNextBtn' id='letterNextBtn'>Sample Word</button>");
        result.append(btn)
    }
    $("#btn_word").append(result)
}

function update(event) {
    $("#audioCurTime").html(transTime(event.currentTime));
}
  
function transTime(value) {
    var time = "";
    var h = parseInt(value / 3600);
    value %= 3600;
    var m = parseInt(value / 60);
    var s = parseInt(value % 60);
    if (h > 0) {
        time = formatTime(h + ":" + m + ":" + s);
    } else {
        time = formatTime(m + ":" + s);
    }
    return time;
}
  
function formatTime(value) {
    var time = "";
    var s = value.split(':');
    var i = 0;
    for (; i < s.length - 1; i++) {
        time += s[i].length == 1 ? ("0" + s[i]) : s[i];
        time += ":";
    }
    time += s[i].length == 1 ? ("0" + s[i]) : s[i];
  
    return time;
}

$(document).ready(function () {
    $("#sound").html(`
      <audio id="originalAudio" ontimeupdate="update(this)">
          <source src="${letter.sound}" type="audio/ogg">
          <source src="${letter.sound}" type="audio/mpeg">
          Your browser does not support the audio element.
      </audio>
      <div class="customAudio" id="customAudio"><i class="fas fa-solid fa-play" style="transform: translateX(5px);"></i></div>
      <div class="time" id="audioCurTime">00:00</div>
    `)

    $("#customAudio").click(function() {
        const customAudio = $("#customAudio");
        const originalAudio = $("#originalAudio").get(0);
        const play = '<i class="fas fa-solid fa-play" style="transform: translateX(5px);" aria-hidden="true"></i>';
        const pause = '<i class="fas fa-solid fa-pause" aria-hidden="true"></i>';
    
        let curState = customAudio.html();
        customAudio.html(curState === play ? pause : play);

        if(curState === play) originalAudio.play();
        else originalAudio.pause();

        originalAudio.addEventListener('ended', function() {
            customAudio.html(play);
        }, false)
    })

    letter_menu(data)
    next_button()
    $("#letterProviousBtn").click(function() {
        i = letter['id']-1
		window.location.href='/letters/'+i
    })
    $("#letterNextBtn").click(function() {
        i = letter['id']+1
        if(i <= 10){
            window.location.href='/letters/'+i
        }
		else{
            window.location.href='/words/1'
        }
    })

});
