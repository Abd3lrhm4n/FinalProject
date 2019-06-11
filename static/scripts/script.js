$('document').ready(function(){
    
    $("#password").focus();
    $(".time").css("display", "none");
    $("#data-info").hide();

    //$('#password').togglePassword();

    // Configure MinSize -- default is 5
    PasswordValidator.minSize = 8;
    // Configure MaxSize -- default is 15
    PasswordValidator.maxSize = 16;

    // whether you want to validate on prohibited characters    
    PasswordValidator.prohibitedConfigured = false;

    PasswordValidator.setup('password');

    // $("#password").on("keyup", function(){

    //     let v = $("#password").val();

    //     // check pw contain number
    //     if(v.match("[0-9]")){
    //         $("li:contains('Must contain a number.')").addClass("valid");
    //         $("li:contains('Must contain a number.')").removeClass("invalid");
    //     }
    //     else{
    //         $("li:contains('Must contain a number.')").addClass("invalid");
    //         $("li:contains('Must contain a number.')").removeClass("valid");
    //     }

    //     // check pw length > 8
    //     if(v.length > 7){
    //         $("li:contains('Must be at least 8 characters long.')").addClass("valid");
    //         $("li:contains('Must be at least 8 characters long.')").removeClass("invalid");
    //     }
    //     else{
    //         $("li:contains('Must be at least 8 characters long.')").addClass("invalid");
    //         $("li:contains('Must be at least 8 characters long.')").removeClass("valid");
    //     }
        
    //     // check pw contain lowercase
    //     if(v.match("[a-z]")){
    //         $("li:contains('Must contain a lowercase letter.')").addClass("valid");
    //         $("li:contains('Must contain a lowercase letter.')").removeClass("invalid");
    //     }
    //     else{
    //         $("li:contains('Must contain a lowercase letter.')").addClass("invalid");
    //         $("li:contains('Must contain a lowercase letter.')").removeClass("valid");

    //     }

    //     // check pw contain uppercase
    //     if(v.match("[A-Z]")){
    //         $("li:contains('Must contain an uppercase letter.')").addClass("valid");
    //         $("li:contains('Must contain an uppercase letter.')").removeClass("invalid");
    //     }
    //     else{
    //         $("li:contains('Must contain an uppercase letter.')").addClass("invalid");
    //         $("li:contains('Must contain an uppercase letter.')").removeClass("valid");
    //     }

    //     // check pw contain special character
    //     if (v.match("[/~/!/@/#/$/%/^/&/*/(/)/_/-/=/|/?/>/<]")){
    //         $("li:contains('special character.')").addClass("valid");
    //         $("li:contains('special character.')").removeClass("invalid");
    //     }
    //     else{
    //         $("li:contains('special character.')").addClass("invalid");
    //         $("li:contains('special character.')").removeClass("valid");
    //     }

    // });

    // $("#password").on("focus", function(){
    //     $("ul").addClass('focus');
    // });

    // $("#password").on("focusout", function(){
    //     $("ul").removeClass("focus");
    // });

    $("input[name=info]").on("change", function() {
        
        $(".userInfo").toggle("slow", "linear");
    });

    //show and hide password
    let showen = false;

    $("#eye").on("click", () =>{
        
        if (showen == false) {
            $("#password").attr('type', 'text');
            $("#eye").css("color", "red");
            showen = true;
        }
        else {
            $("#password").attr('type', 'password');
            $("#eye").css("color", "black");
            showen = false;
        }
    });

    $("#password").on("focus", function() {
        $(".popover").show();
    })
    $("#password").on("focusout", () => {
        $(".popover").hide();
    })
});


