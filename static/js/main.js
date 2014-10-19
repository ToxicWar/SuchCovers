var params=[
	{							//получить все обложки
		type: 'GET',
		adress: '/api/covers/'
	}
],
incomeHandlers=[				//обработать все обложки
	handleFullList
], 
fullList=''

document.onreadystatechange = function () {
    if (document.readyState == "complete") {
        init();
    }
}
function init(){
	load(0)
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
	for(var i=0; i<document.getElementsByClassName('cb_image');i++){
		document.getElementsByClassName('cb_image')[i].addEventListener('click', popupFullCover)
	}
}
function popupFullCover(e){
	var cover_id = e.target.getAttribute('data');
	fullPopupCover.setAttribute('class', 'fpc_visible')
}