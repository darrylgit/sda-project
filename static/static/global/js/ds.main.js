var flatpage = flatpage || {};

var isFirstLoad = function(namesp, jsFile) {
	var isFirst = namesp.firstLoad === undefined;
	namesp.firstLoad = false;

	if (!isFirst) {
		console.log("warning: javascript file is included twice: " + jsFile);
	}

	return isFirst;
};
