$(document).ready(function(){
    const checkedRadio = data && data.selected;
    if(checkedRadio) {
        $(".form-check-input").each(function(i, item) {
            if($(item).attr("value") === checkedRadio) {
                $(item).attr("checked", "checked");
            }
            if($(item).attr("checked") === "checked"){
                $(item).css("background-color", data.result === 0 ? "red" : "#6AA84F");
                $(item).css("border-color", data.result === 0 ? "red" : "#6AA84F");
            }
        })
    }
    // incorrect selection
    if(data && data.result === 0) {
        $("#resultInfo").html(`
                                <p style="color: red; font-size: 18px;">Sorry, your answer is <b>INCORRECT.</b></p>
                                <p style="color: #5E5E5E; font-size: 18px;">The right answer is <b>${data.rightAwswer}</b></p>
                                `);
    } else if(data && data.result === 1) {  // correct selection
        $("#resultInfo").html(`
                                <p style="color: #6AA84F; font-size: 18px;">Yeah! Your answer is <b>CORRECT!</b></p>
                                <p style="color: #5E5E5E; font-size: 18px;">The right answer is <b>${data.rightAwswer}</b></p>
                                `);
    }

    $("#quiz01Next").click(function() {
        window.location.href = `/quiz/02`;
    })
})