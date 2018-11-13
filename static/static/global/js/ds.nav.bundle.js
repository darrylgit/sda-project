(function() {
    function drawerCollapseHandler() {
        $("#drawer").addClass("active");
        // create button if non existent
    }
    function addCollapseHandler() {
        // fade in the overlay
        $(".overlay").addClass("active");
        // prevent page scrolling
        $("body").css({ overflow: "hidden" });
    }

    function removeCollapseHandler() {
        [$("#drawer"), $(".overlay")].forEach(function(element) {
            element.removeClass("active");
        });
        // page scrolling
        $("body").css({ overflow: "scroll" });
    }

    // add toggle button to DOM
    function togglerElementDOM() {
        var button = document.createElement("button");
        $(button).attr({
            type: "button",
            id: "drawerCollapse",
            class: "navbar-toggler p-0"
        });
        // create div element instance
        // create dismiss icon with div element instance
        // place instances inside button wrapper
        for (i = 0; i < 2; i++) {
            div = document.createElement("div");
            div.setAttribute("class", "icon-bar");
            button.appendChild(div);
        }
        // middle bar adds padding
        div = document.createElement("div");
        div.setAttribute("class", "icon-bar icon-bar-m");
        //insert as middle bar
        $(div).insertAfter($(button).children()[0]);

        if (window.matchMedia("(max-width: 576px)").matches) {
            $(button).addClass("max576");
            $("#toggler nav")[0].appendChild(button);
        } else if (!window.matchMedia("(max-width: 576px)").matches) {
            // add breakpoint class and space between icon and brand name
            $(button).addClass("min576 mr-2");
            $(button).prependTo($("#toggler nav div:nth-child(1)")[0]);
        }
    }

    // add dismiss button to DOM
    function drawerElementDOM() {
        // create button
        var button = document.createElement("button");
        $(button).attr({
            type: "button",
            class: "navbar-toggler p-0"
        });

        if (window.matchMedia("(max-width: 576px)").matches) {
            /*
            //generate an x icon - left and right diagonal lines 
            //right diagonal css inherits dimensions of left diagonal
            //wrap x icon to retain same margin as 3 bars icon, inherits button dimensions
            */

            // create wrapper for x button
            var xWrapper = document.createElement("div");
            $(xWrapper).attr({
                id: "xWrapper"
            });

            //create left diagonal and append to wrapper
            div = document.createElement("div");
            div.setAttribute("class", "bar-xl");
            $(xWrapper)[0].appendChild(div);

            //create right diagonal and append to left diagonal div
            div = document.createElement("div");
            div.setAttribute("class", "bar-xr");
            $(xWrapper)
                .children(".bar-xl")[0]
                .appendChild(div);
            // append wrapper to button
            $(button)[0].appendChild(xWrapper);
            // add breakpoint class
            $(button).addClass("max576");
            //place button in DOM
            $("#drawer nav")[0].appendChild(button);
        } else if (!window.matchMedia("(max-width: 576px)").matches) {
            /*
            //generate 3 bars icon - 3 horizonal divs, add spacing between 
            */

            // create outer bars and append to button
            for (i = 0; i < 2; i++) {
                div = document.createElement("div");
                div.setAttribute("class", "icon-bar");
                button.appendChild(div);
            }

            // create middle bar with top and bottom margin
            div = document.createElement("div");
            div.setAttribute("class", "icon-bar icon-bar-m");
            $(div).insertAfter($(button).children()[0]);

            // add breakpoint class with space after
            $(button).addClass("min576 mr-2");
            //place button in DOM
            $(button).prependTo($("#drawer nav div")[0]);
        }

        //signal drawer listener
        // on-fly event listener, doesn't work outside this function idk
        drawerElementListener();
    }

    function drawerElementListener() {
        removeCollapse = [$("#drawer nav button")[0], $(".overlay")[0]].forEach(
            function(element) {
                element.addEventListener("click", removeCollapseHandler);
            }
        );
    }

    function togglerElementListeners() {
        // window resize
        // on-fly listeners
        drawerCollapse = document
            .getElementById("drawerCollapse")
            .addEventListener("click", drawerCollapseHandler);

        addCollapse = document
            .getElementById("drawerCollapse")
            .addEventListener("click", addCollapseHandler);
    }

    function breakpoint() {
        // window resize
        // 576px breakpoint
        if (
            $("#drawer nav button").hasClass("max576") &&
            $("#toggler nav button").hasClass("max576")
        ) {
            // remove change class when window exceeds 576px
            if (!window.matchMedia("(max-width: 576px)").matches) {
                //remove button
                $("#drawer nav button").remove();
                drawerElementDOM();
                $("#toggler nav")
                    .children("button")
                    .remove();
                togglerElementDOM();
            }
        } else if (
            $("#drawer nav button").hasClass("min576") &&
            $("#toggler nav div:nth-child(1) button").hasClass("min576")
        ) {
            if (window.matchMedia("(max-width: 576px)").matches) {
                $("#drawer nav div button").remove();
                drawerElementDOM();
                $("#toggler nav div:nth-child(1) button").remove();
                togglerElementDOM();
            }
        }
    }

    // window resize
    var resizeHandler = function() {
        breakpoint();
        togglerElementListeners();
    };

    $(window).resize(resizeHandler);

    // place dismiss button in DOM before setting listeners
    document.addEventListener("DOMContentLoaded", togglerElementDOM, false);
    window.addEventListener("DOMContentLoaded", togglerElementListeners, false);
    window.addEventListener("DOMContentLoaded", drawerElementDOM, false);
})();
