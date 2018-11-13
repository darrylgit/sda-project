(function() {
    function searchCollapseHandler() {
        // show search form
        $("#search").addClass("active");
    }
    function addSearchCollapseHandler() {
        // fade in the overlay
        $(".overlay").addClass("active");
        // prevent page scrolling
        $("body").css({ overflow: "hidden" });
    }

    function removeSearchCollapseHandler() {
        [$("#search"), $(".overlay")].forEach(function(element) {
            element.removeClass("active");
        });
        // page scrolling
        $("body").css({ overflow: "scroll" });
    }

    //set event listeners
    function searchTogglerListeners() {
        searchCollapse = document
            .getElementById("searchCollapse")
            .addEventListener("click", searchCollapseHandler);
        addSearchCollapse = document
            .getElementById("searchCollapse")
            .addEventListener("click", addSearchCollapseHandler);
        removeSearchCollapse = [$("#remove-search"), $(".overlay")].forEach(
            function(element) {
                element[0].addEventListener(
                    "click",
                    removeSearchCollapseHandler
                );
            }
        );
    }

    // place dismiss button in DOM before setting listeners
    window.addEventListener("DOMContentLoaded", searchTogglerListeners, false);
})();
