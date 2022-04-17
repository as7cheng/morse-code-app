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

$(document).ready(function () {
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
