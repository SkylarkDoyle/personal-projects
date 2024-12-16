var sidebarOpen = false;
var footerLinksDis = false;
var footerLinksDis = false;

var toggle = function() {

var sidebar = document.querySelector("#sidebar");

    if(sidebarOpen === false){
      sidebar.style.width = "80%";
       sidebar.style.opacity = "1"
       sidebarOpen = true
    }

    else if (sidebarOpen === true){
        sidebar.style.width = "5%";
        sidebar.style.opacity = "0"
        sidebarOpen = false;
    }

}

var linksToggleOne = function (){
    var footerHeader = document.querySelectorAll(".footer-header")[0]
    var footerHeaderH5 = document.querySelectorAll(".footer-header h5")[0]
    var footerHeaderSpan = document.querySelectorAll(".footer-header span")[0]
    var footerlinks = document.querySelectorAll(".footer-links ul:nth-child(1) li");

    if(footerLinksDis === false){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'block'
            
        }
        footerHeader.style.backgroundColor = "#555555"
        footerHeaderH5.style.color = "#fff"
        footerHeaderSpan.style.transform = "rotate(45deg)"
        footerLinksDis = true;
    }

   else if(footerLinksDis === true){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'none'
        }
        footerHeader.style.backgroundColor = "#000000"
        footerHeaderH5.style.color = "rgb(255, 255, 255, 0.4)"
        footerHeaderSpan.style.transform = "rotate(0deg)"
        footerLinksDis = false;
    }

}


var linksToggleTwo = function (){
    var footerHeader = document.querySelectorAll(".footer-header")[1]
    var footerHeaderH5 = document.querySelectorAll(".footer-header h5")[1]
    var footerHeaderSpan = document.querySelectorAll(".footer-header span")[1]
    var footerlinks = document.querySelectorAll(".footer-links ul:nth-child(2) li");

    if(footerLinksDis === false){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'block'
        }
        footerHeader.style.backgroundColor = "#555555"
        footerHeaderH5.style.color = "#fff"
        footerHeaderSpan.style.transform = "rotate(45deg)"
        footerLinksDis = true;
    }

   else if(footerLinksDis === true){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'none'
        }
        footerHeader.style.backgroundColor = "#000000"
        footerHeaderH5.style.color = "rgb(255, 255, 255, 0.4)"
        footerHeaderSpan.style.transform = "rotate(0deg)"
        footerLinksDis = false;
    }

}


var linksToggleThree = function (){
    var footerHeader = document.querySelectorAll(".footer-header")[2]
    var footerHeaderH5 = document.querySelectorAll(".footer-header h5")[2]
    var footerHeaderSpan = document.querySelectorAll(".footer-header span")[2]
    var footerlinks = document.querySelectorAll(".footer-links ul:nth-child(3) li");

    if(footerLinksDis === false){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'block'
        }
        footerHeader.style.backgroundColor = "#555555"
        footerHeaderH5.style.color = "#fff"
        footerHeaderSpan.style.transform = "rotate(45deg)"
        footerLinksDis = true;
    }

   else if(footerLinksDis === true){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'none';
        }
        footerHeader.style.backgroundColor = "#000000";
        footerHeaderH5.style.color = "rgb(255, 255, 255, 0.4)";
        footerHeaderSpan.style.transform = "rotate(0deg)"
        footerLinksDis = false;
    }

}

var linksToggleFour = function (){
    var footerHeader = document.querySelectorAll(".footer-header")[3]
    var footerHeaderH5 = document.querySelectorAll(".footer-header h5")[3]
    var footerHeaderSpan = document.querySelectorAll(".footer-header span")[3]
    var footerlinks = document.querySelectorAll(".footer-links ul:nth-child(4) li");

    if(footerLinksDis === false){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'block'
        }
        footerHeader.style.backgroundColor = "#555555"
        footerHeaderH5.style.color = "#fff"
        footerHeaderSpan.style.transform = "rotate(45deg)"
        footerLinksDis = true;
    }

   else if(footerLinksDis === true){
        for (let i = 0; i < footerlinks.length; i++) {   
            footerlinks[i].style.display = 'none';
        }
        footerHeader.style.backgroundColor = "#000000";
        footerHeaderH5.style.color = "rgb(255, 255, 255, 0.4)";
        footerHeaderSpan.style.transform = "rotate(0deg)"
        footerLinksDis = false;
    }

}
