
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

$(document).ready(function(){
  $("#sound").html(`
      <audio id="originalAudio" ontimeupdate="update(this)">
          <source src="../static/assert/morse_code_sounds/mcs-hope.wav" type="audio/ogg">
          <source src="../static/assert/morse_code_sounds/mcs-hope.wav" type="audio/mpeg">
          Your browser does not support the audio element.
      </audio>
      <div class="customAudio" id="customAudio"><i class="fas fa-solid fa-play" style="transform: translateX(5px);"></i></div>
      <div><span class="time" id="audioCurTime">00:00</span></div>
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

  $("#wordProviousBtn").click(function() {
		window.location.href='/letters/10'
  })

  $("#wordNextBtn").click(function() {
      window.location.href='/words/2'
  })
})