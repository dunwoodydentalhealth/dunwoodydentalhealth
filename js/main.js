(function(){
var btn=document.querySelector('.menu-btn'),nav=document.querySelector('.site-header .nav');
if(btn){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o)})}
var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
var f=document.querySelector('.form');
if(f){f.addEventListener('submit',function(e){
var ok=f.name.value.trim()&&/^\S+@\S+\.\S+$/.test(f.email.value)&&f.message.value.trim();
f.querySelector('.err').hidden=!!ok;if(!ok)e.preventDefault()})}
})();
