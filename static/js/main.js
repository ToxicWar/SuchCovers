var params=[
	{							//получить все обложки
		type: 'GET',
		adress: '/api/covers/'
	}
],
incomeHandlers=[				//обработать все обложки
	handleFullList
], 
fullList='',
scrn_width = 0, scrn_height = 0


document.onreadystatechange = function () {
    if (document.readyState == "complete") {
        init();
    }
}
function init(){
	load(0)
	initScreenSize()
	blackScreen.addEventListener('click', closePopup)
}
function initScreenSize(){
	scrn_width = screen.width
	scrn_height = screen.height
}

function load(param){
	//loading.setAttribute("class","visible");
	
    xmlhttp = new XMLHttpRequest();    
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
			var income = JSON.parse(xmlhttp.responseText);
			fullList = income
			incomeHandlers[param](income)
        }
    }   
    xmlhttp.open(params[param].type, params[param].adress, true);
    xmlhttp.send();  
}
/*                       incomeHandlers                        */
function handleFullList(income){
	var html=''
	for (var i=0; i<income.results.length; i++){
		html += addCover(income.results[i])
	}
	ic.innerHTML = html;
	//loading.setAttribute("class","hidden");
	//content.setAttribute("class", "")
	function addCover(rawCover){
		var resultStr = '<div class="cover_block f_l"><div class="cb_image" data="'+rawCover.id+'" style="background:url(&quot;'+rawCover.image+ '&quot;); background-size:100%"></div><div class="cb_buttons"><div class="cd_but f_l">л</div><div class="cd_but f_l">ш</div><div class="cd_but f_l">к</div></div></div>'
		return resultStr
	}
	for(var i=0; i<document.getElementsByClassName('cb_image').length;i++){
		document.getElementsByClassName('cb_image')[i].addEventListener('click', popupFullCover)
	}
}
function popupFullCover(e){
	blackScreen.setAttribute('class', 'visible')
	var cover_id = e.target.getAttribute('data')
	fullPopupCover.setAttribute('class', 'fpc_visible')
	fullPopupCover.style.top = scrn_height/2 - 250 +'px'
	fullPopupCover.style.left = scrn_width/2 - 250 +'px'
}
function closePopup(){
	fullPopupCover.setAttribute('class', 'fpc_hidden')
	blackScreen.setAttribute('class', 'hidden')
}