const start = async ()=>{
    const container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
    const { divisions } = await fetch(
        "./map_json.json"
    ).then((response) => response.json());
    const result_list = document.querySelector(".result_list")

    let options = { //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
        level: 3 //지도의 레벨(확대, 축소 정도)
    };
    let map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴



    function panTo(latitude, longitude, name) {
        const show = ()=>{
            infowindow.open(map, marker);
        }
        // 이동할 위도 경도 위치를 생성합니다 
        map.setLevel(3);
        var moveLatLon = new kakao.maps.LatLng(latitude, longitude);
        
        // 지도 중심을 부드럽게 이동시킵니다
        // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
        map.panTo(moveLatLon);
        
        var markerPosition = new kakao.maps.LatLng(latitude, longitude); 
        var marker = new kakao.maps.Marker({
            position: markerPosition,
            clickable: true
        });

        marker.setMap(map);
        var iwPosition  = new kakao.maps.LatLng(latitude, longitude); 
        var iwContent = `<div style="padding:5px;">${name}</div>`;
        // 마커를 생성합니다
        var infowindow = new kakao.maps.InfoWindow({
            position : iwPosition,
            content : iwContent,
            removable : true
        });
        show()
        kakao.maps.event.addListener(marker, 'click', show);
    }
    const search_input = document.querySelector(".search_input")
    const search_button = document.querySelector(".search_button")

    function moveMap(){
        if(search_input.value.trim() === "")return;
        let test = divisions.filter(e => e.name.includes(search_input.value))
        panTo(test[0].latitude , test[0].longitude, test[0].name);
    }


    search_button.addEventListener("click", moveMap)


    search_input.addEventListener("input" , (e) => {
        let value = search_input.value
        // console.log(e.keycode)
        result_list.innerHTML = ""
        if(value.trim() === "")return;
        let result = JSON_search(value)
        result.forEach(element => {
            const result_element = document.createElement("li")
            result_element.classList.add("extra")
            result_element.textContent = element.name
            // console.log(result_list)
            result_list.append(result_element)
        });
        // console.log(e.target)
        if(e.key === 'Enter') moveMap;
    })

    let arr2 = [];
    function JSON_search(value){
        if(value.trim() === "")return;
        let arr = divisions.filter(e => e.name.includes(value))
        // console.log(arr)
        // console.log(arr.length)
        if(arr.length-1 >= 10) {
            arr2 = arr.slice(0, 10)
            return arr2
        }
        return arr
    }
}
start()
const search_ul = document.querySelector("ul.result_list");
const search_input = document.querySelector(".search_input");
search_input.addEventListener("focus",(e)=>{
    search_ul.classList.remove("off_ul");
    console.log(search_ul)
})
search_input.addEventListener("blur",(e)=>{
    search_ul.classList.add("off_ul");
    console.log(search_ul)
})