/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: http://creative-tim.com
 * 
 */

$("#top-bar__sign-inn").on("click", function(e){
    e.preventDefault();
  $('#modalholder').load('/login');
  openLoginModal();


});

function formSubmit(){

$("#LoginFormId").on("submit", function(event){
    event.preventDefault();
    alert('form submitted!')
    console.log("form submitted!"
    ajaxPost();
});

}




// ************************THIS IS FOR SIDE NAVE MOB**********************

$("#signin-sidenav").on("click", function(){
 resetNav1();
  $('#modalholder').load('/login');
  openLoginModal();
});

function resetNav1() {
    $('#nav-icon-toggle').removeClass('nav-icon-toggle--is-open');
    $('#sidenav').removeClass('sidenav--is-open');
    $('#main').removeClass('main--is-open');
  }

// ---------------------------- END ----------------------------






function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    }); 
    $('.error').removeClass('alert alert-danger').html('');
       
}
function showLoginForm(){
    $('#loginModal .registerBox').fadeOut('fast',function(){
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');    
        });
        
        $('.modal-title').html('Login with');
    });       
     $('.error').removeClass('alert alert-danger').html(''); 
}

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230);
    
}
function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
        $('#loginModal').modal('show');    
    }, 230);
    
}



function shakeModal(){
    $('#loginModal .modal-dialog').addClass('shake');
             $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
             $('input[type="password"]').val('');
             setTimeout( function(){ 
                $('#loginModal .modal-dialog').removeClass('shake'); 
    }, 1000 ); 
}

   