(function JcImagesTooltipModule(factory) {
    "use strict";

    window.JcImagesTooltip = factory();
})(function JcImagesTooltipFactory() {
    /**
     * @class  JcImagesTooltip
     * @param  {selector} selector
     * @param  {Object} [options]
     */
    function JcImagesTooltip(selector, options) {
        // Bind all private methods
        for (var fn in this) {
            if (fn.charAt(0) === '_' && typeof this[fn] === 'function') {
                this[fn] = this[fn].bind(this);
            }
        }

        var defaults = {
            width: 430,
            height: 320,
            offset: 10
        };

        this.selector = selector;
        this.options = _extend(defaults, options);

        this._createContainer();

        var elements = document.querySelectorAll(selector);

        if (elements.length > 0) {
            for (var i = 0; i < elements.length; i++) {
                var self = this;
                var img = elements[i];

                if (typeof img.dataset.processed === 'undefined') {
                    img.setAttribute('data-processed', true);

                    _on(img, 'mouseover', function() {
                        self.options.current = this;
                        self._showHandler();
                    });
                    _on(img, 'mouseleave', function() {
                        self.options.current = null;
                        self._closeHandler();
                    });
                }
            }
        }
    }

    JcImagesTooltip.prototype = {
        constructor: JcImagesTooltip,
        selector: null,
        container: null,
        current: null,
        _createContainer: function() {
            var options = this.options;

            if (this.container === null) {
                var tooltip = document.createElement('div');
                tooltip.classList.add('thumb-tooltip');
                tooltip.style.width = options.width + 'px';
                tooltip.style.height = options.height + 'px';
                tooltip.style.display = 'none';

                var tooltipImage = document.createElement('div');
                tooltipImage.classList.add('thumb-tooltip-image');

                tooltip.append(tooltipImage);
                document.body.append(tooltip);

                this.container = {
                    tooltip: tooltip,
                    tooltipImage: tooltipImage
                };
            }

            return this.container;
        },
        _showHandler: function() {
            var options = this.options;
            var current = options.current;
            var container = this.container;
            var offset = options.offset;

            var coords = getCoords(current);
            var rect = current.getBoundingClientRect();

            var document_scroll_left = window.pageXOffset || document.documentElement.scrollLeft;
            var document_scroll_top = window.pageYOffset || document.documentElement.scrollTop;

            var document_width = document_scroll_left + document.documentElement.clientWidth;
            var document_height = document_scroll_top + document.documentElement.clientHeight;

            var x1 = coords.left;
            var x2 = coords.left + rect.width;

            var y1 = coords.top;
            var y2 = coords.top + rect.height;

            container.tooltipImage.style.backgroundImage = 'url(' + current.dataset.src + ')';

            var container_left = x2 + offset;
            var container_top = y1;
            var container_width = options.width;
            var container_height = options.height;

            if (document_height < (container_top + container_height)) {
                container_top = document_height - container_height;
            } else if (document_scroll_top > container_top) {
                container_top = document_scroll_top;
            }

            if (document_width < (container_left + container_width)) {
                container_left = x1;

                if (document_width < (container_left + container_width)) {
                    container_left = document_width - container_width;
                }

                if (document_height > y2 + container_height) {
                    container_top = y2 + offset;
                } else {
                    container_top = y1 - container_height - offset;
                }

                if (document_scroll_top > container_top) {
                    container_top = y1;
                    container_left = x1 - container_width - offset;

                    if (document_height < (container_top + container_height)) {
                        container_top = document_height - container_height;
                    } else if (document_scroll_top > container_top) {
                        container_top = document_scroll_top;
                    }
                }
            }

            container.tooltip.style.left = container_left + 'px';
            container.tooltip.style.top = container_top + 'px';
            container.tooltip.style.display = '';
        },
        _closeHandler: function() {
            this.container.tooltip.style.display = 'none';
        },
        update: function() {
            new JcImagesTooltip(this.selector, this.options);
        }
    }

    function _extend(dst, src) {
        if (dst && src) {
            for (var key in src) {
                if (src.hasOwnProperty(key)) {
                    dst[key] = src[key];
                }
            }
        }

        return dst;
    }

    function _on(element, event, fn) {
        element.addEventListener(event, fn, {
            capture: false,
            passive: false
        });
    }

    function getCoords(elem) {
        // (1)
        var box = elem.getBoundingClientRect();

        var body = document.body;
        var docEl = document.documentElement;

        // (2)
        var scrollTop = window.pageYOffset || docEl.scrollTop || body.scrollTop;
        var scrollLeft = window.pageXOffset || docEl.scrollLeft || body.scrollLeft;

        // (3)
        var clientTop = docEl.clientTop || body.clientTop || 0;
        var clientLeft = docEl.clientLeft || body.clientLeft || 0;

        // (4)
        var top = box.top + scrollTop - clientTop;
        var left = box.left + scrollLeft - clientLeft;

        return {
            top: top - 50,
            left: 500
        };
    }

    /**
     * Create JcImagesTooltip instance
     * @param {selector} selector
     * @param {Object} [options]
     */
    JcImagesTooltip.create = function(selector, options) {
        return new JcImagesTooltip(selector, options);
    };

    // Export
    return JcImagesTooltip;
});