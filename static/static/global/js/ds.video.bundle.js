(function() {
	function playlistVideoEventHandler(e, elem) {
		e.preventDefault();
		videotarget = elem.getAttribute("href");
		filename =
			videotarget.substr(0, videotarget.lastIndexOf(".")) || videotarget;
		video = document.querySelector("#playlist-video-main video");
		source = document.querySelectorAll("#playlist-video-main video source");
		source[0].src = filename + ".mp4";
		source[1].src = filename + ".webm";
		video.load();
		//video.play();
	}
	function playlistVideoInfoEventHandler(elem) {
		videoinfotarget = elem.getElementsByTagName("p");
		title = videoinfotarget[0].getAttribute("href");
		desc = videoinfotarget[1].getAttribute("href");
		document.querySelector("#video-main-title").innerHTML = title;
		document.querySelector("#video-main-description").innerHTML = desc;
	}

	function playlistEventListener() {
		var video_player = document.getElementById("playlist-video-secondary"),
			links = video_player.getElementsByTagName("a");
		for (var i = 0; i < links.length; i++) {
			links[i].onclick = function(e) {
				playlistVideoEventHandler(e, this);
				playlistVideoInfoEventHandler(this);
			};
		}
	}

	document.addEventListener("DOMContentLoaded", playlistEventListener);
})();
