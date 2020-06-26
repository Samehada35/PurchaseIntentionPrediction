function getOS(){
    let os = ["Windows 10","Windows 8","Windows 7","Windows Vista","Windows XP","Windows 2000","Mac/iOS","UNIX","Linux","Uknown"];
    let userInfos = window.navigator.userAgent;
    
    if (userInfos.indexOf("Windows NT 10.0")!= -1) return 0;
    if (userInfos.indexOf("Windows NT 6.2")!= -1) return 1;
    if (userInfos.indexOf("Windows NT 6.1")!= -1) return 2;
    if (userInfos.indexOf("Windows NT 6.0")!= -1) return 3;
    if (userInfos.indexOf("Windows NT 5.1")!= -1) return 4;
    if (userInfos.indexOf("Windows NT 5.0")!= -1) return 5;
    if (userInfos.indexOf("Mac")!= -1) return 6;
    if (userInfos.indexOf("X11")!= -1) return 7;
    if (userInfos.indexOf("Linux")!= -1) return 8;
    return 9;
}

function getBrowser(){
    let browsers = ["Chrome","IE","Firefox","Opera","Safari","Edge","Uknown"];
    let userInfos = window.navigator.userAgent;
    
    if (userInfos.indexOf("Chrome")!= -1) return 0;
    if ((userInfos.indexOf("MSIE")!= -1) || !!document.documentMode) return 1;
    if (userInfos.indexOf("Firefox")!= -1) return 2;
    if ((userInfos.indexOf("Opera")|| navigator.userAgent.indexOf('OPR'))!= -1) return 3;
    if (userInfos.indexOf("Safari")!= -1) return 4;
    if (userInfos.indexOf("Edge")!= -1) return 5;
    return 6;
}

function getRegion(position){
    let regions = ["Americas","Europe","Asia","Oceania","Africa","Northern Europe","Central Europe","Eastern Europe","Southern Europe"];
    
       let lat = position.coords.latitude;
       let lon = position.coords.longitude;
    
       if(lat<37 && lat>-37 && lon > -17 && lon < 51) return 4;
       if(lat>37 && lon > -13 && lon < 33) return 1;
       if(lat>-7 && lon > 27 && lon < 180) return 2;
       if(lat>-40 && lat<0 && lon > 110 && lon < 152) return 3;
       else return 0;

}

function getMonth(){
    let date = new Date();
        
    return date.getMonth();    
}

function isWeekend(){
    let day = new Date().getDay();
    
    return day==0||day==6 ? 0 : 1;
}

function isReturningVisitor(){
    if(window.localStorage.getItem('visited') === "true"){
        return 1;
    }else{
        window.localStorage.setItem('visited',"true");
        return 0;
    }
}

function specialDay(){
    let currentYear = new Date().getFullYear();
    let specialDays=[new Date(currentYear+1,0,1),
                     new Date(currentYear,1,14),
                     new Date(currentYear,2,8),
                     new Date(currentYear,3,1),
                     new Date(currentYear,3,12),
                     new Date(currentYear,4,1),
                     new Date(currentYear,4,10),
                     new Date(currentYear,5,16),
                     new Date(currentYear,9,31),
                     new Date(currentYear,11,25)];
    let currentDate = new Date();
    
    let maxCloseness = 0;
    
    for(let i=0;i<specialDays.length;i++){
        let diffTime = specialDays[i].getTime() - currentDate.getTime();
        let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
        if(diffDays>=0 && diffDays<=10){
            let closeness = (10-diffDays)/10;
            
            if(closeness>maxCloseness){
                maxCloseness = closeness;
            }
        }
    }
 
    return maxCloseness;

}

function getTrafficType(){
    let trafficSources = ["Direct","Referral","Search","Campaign"];
    return 0;
}

function getInputArray(position){
    return ['null',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
            specialDay(),
            getMonth(),
            getOS(),
            getBrowser(),
            getRegion(position),
            getTrafficType(),
            isReturningVisitor(),
            isWeekend()];
}
        
var outputDiv= document.getElementById('test');
 
window.navigator.geolocation.getCurrentPosition(function(position) {
    if(position){
        outputDiv.innerHTML = getInputArray(position);
    }else{
     position = { cords : {
                    latitude : 0, 
                    longitude : 0
                }
     };
     outputDiv.innerHTML = getInputArray(position);
    }
    
    }, function(error) {
     position = { coords : {
                    latitude : 0, 
                    longitude : 0
                }
     };
     outputDiv.innerHTML = getInputArray(position);
});
