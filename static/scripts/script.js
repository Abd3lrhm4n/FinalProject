$('document').ready(function(){
    
    $("#password").focus();

    $("#password").on("keyup", function(){

        let v = $("#password").val();

        // check pw contain number
        if(v.match("[0-9]")){
            $("li:contains('Must contain a number.')").addClass("valid");
            $("li:contains('Must contain a number.')").removeClass("invalid");
        }
        else{
            $("li:contains('Must contain a number.')").addClass("invalid");
            $("li:contains('Must contain a number.')").removeClass("valid");
        }

        // check pw length > 8
        if(v.length > 7){
            $("li:contains('Must be at least 8 characters long.')").addClass("valid");
            $("li:contains('Must be at least 8 characters long.')").removeClass("invalid");
        }
        else{
            $("li:contains('Must be at least 8 characters long.')").addClass("invalid");
            $("li:contains('Must be at least 8 characters long.')").removeClass("valid");
        }
        
        // check pw contain lowercase
        if(v.match("[a-z]")){
            $("li:contains('Must contain a lowercase letter.')").addClass("valid");
            $("li:contains('Must contain a lowercase letter.')").removeClass("invalid");
        }
        else{
            $("li:contains('Must contain a lowercase letter.')").addClass("invalid");
            $("li:contains('Must contain a lowercase letter.')").removeClass("valid");

        }

        // check pw contain uppercase
        if(v.match("[A-Z]")){
            $("li:contains('Must contain an uppercase letter.')").addClass("valid");
            $("li:contains('Must contain an uppercase letter.')").removeClass("invalid");
        }
        else{
            $("li:contains('Must contain an uppercase letter.')").addClass("invalid");
            $("li:contains('Must contain an uppercase letter.')").removeClass("valid");
        }

        // check pw contain special character
        if (v.match("[/~/!/@/#/$/%/^/&/*/(/)/_/-/=/|/?/>/<]")){
            $("li:contains('special character.')").addClass("valid");
            $("li:contains('special character.')").removeClass("invalid");
        }
        else{
            $("li:contains('special character.')").addClass("invalid");
            $("li:contains('special character.')").removeClass("valid");
        }

    });

    $("#password").on("focus", function(){
        $("ul").addClass('focus');
    });

    $("#password").on("focusout", function(){
        $("ul").removeClass("focus");
    });

    $("input[name=info]").on("change", function() {
        
        $(".userInfo").toggle("slow", "linear");
    });

    $(".GaugeMeter").gaugeMeter({
        percent : 80,
        text : "Bruteforce Time",
        text_size : 0.22,
        //append : "Years",
        prepend: null,
        size : "500",
        width : 15,
        style : "Arch",
        theme : "Red-Gold-Green",
        animate_gauge_colors : false,
        animate_text_colors : false
    });

});


