$(document).ready(function(){
    // initial submit button
    $("#quizResultPrompt").empty();
    $("#quizSubmitBtn").empty();
    $("#quizSubmitBtn").html(`<button type="submit" class="btn btn-warning">Submit</button>`);

    $("#formSingle").ajaxForm(data => {
        console.log('result =', data)

        // get which one is checked
        $(".form-check-input").each(function(i, item) {
            $(item).attr("disabled", "disabled");
            if($(item).attr("value") === data.checked) {
                $(item).attr("checked", "checked");
            }
            if($(item).attr("checked") === "checked"){
                $(item).css("background-color", data.correctness ? "#6AA84F" : "red");
                $(item).css("border-color", data.correctness ? "#6AA84F" : "red");
            }
        })

        // if the answer is true
        if(data && data.correctness) {
            $("#quizResultPrompt").empty();
            $("#quizResultPrompt").html(`
                <p style="color: #6AA84F; font-size: 16px;">Yeah! Your answer is <b>CORRECT!</b></p>
                <p style="color: #5E5E5E; font-size: 16px;">The right answer is <b>${data.ans}</b></p>
            `);
        } else { // if the answer is false
            $("#quizResultPrompt").empty();
            $("#quizResultPrompt").html(`
                <p style="color: red; font-size: 16px;">Sorry, your answer is <b>INCORRECT.</b></p>
                <p style="color: #5E5E5E; font-size: 16px;">The right answer is <b>${data.ans}</b></p>
            `);
        }

        $("#quizSubmitBtn").empty();
        $("#quizSubmitBtn").html(`<button type="button" class="btn btn-warning" id="quizNext">Next</button>`);

        $("#quizScore").html(`Scores: ${data.scores}`);

        $("#quizNext").click(function() {
            window.location.href = `/quiz/6`;
        })
    });
})