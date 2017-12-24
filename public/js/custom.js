var assignees_divs = $(".select-assignee").find(".item[data-id]");
$("#assignee-filter").val("");
$("#assignee-filter").on("keyup", function(ev){
    if (ev.which == 13) {
        $.each(assignees_divs, function(i, div){
            div = $(div);
            if(div.is(":visible")){
                div.click();
                return false;
            };
        });
    }
    var name = $(this).val().toLowerCase();
    $.each(assignees_divs, function(i, div){
        div = $(div);
        if(div.text().toLowerCase().indexOf(name) >= 0) {
            div.show();
        } else {
            div.hide();
        }
    });
});
