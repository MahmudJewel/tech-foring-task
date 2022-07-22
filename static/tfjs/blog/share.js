/*!
 * loltgt/ensemble.SocialShare
 *
 * @version 0.0.1
 * @link https://github.com/loltgt/ensemble-social-share
 * @copyright Copyright (C) Leonardo Laureti
 * @license MIT License
 */
!(function (e, t) {
    if ("function" == typeof define && define.amd) define(["exports"], t);
    else if ("undefined" != typeof exports) t(exports);
    else {
        var s = { exports: {} };
        t(s.exports), (e.ensemble = s.exports);
    }
})("undefined" != typeof globalThis ? globalThis : "undefined" != typeof self ? self : this, function (e) {
    "use strict";
    Object.defineProperty(e, "__esModule", { value: !0 }), (e.SocialShare = void 0);
    const t = "undefined" == typeof Symbol ? 0 : Symbol,
        s = /html|head|body|meta|link|style|script/i,
        n = /(<(html|head|body|meta|link|style|script)*>)/i;
    const i = /html|head|body|meta|link|style|script/i,
        o = /attributes|classList|innerHTML|outerHTML|nodeName|nodeType/;
    class Compo extends class _composition {
        _renderer() {
            delete this._element, delete this._renderer;
        }
        install(e, t) {
            return "function" == typeof t && t.call(this, this[this._ns]), !!e.appendChild(this[this._ns]);
        }
        uninstall(e, t) {
            return "function" == typeof t && t.call(this, this[this._ns]), !!e.removeChild(this[this._ns]);
        }
        up(e, t) {
            return "function" == typeof t && t.call(this, this[this._ns]), !!e.replaceWith(this[this._ns]);
        }
        append(e) {
            const t = this._ns;
            return !!this[t].appendChild(e[t]);
        }
        prepend(e) {
            const t = this._ns;
            return !!this[t].prependChild(e[t]);
        }
        remove(e) {
            const t = this._ns;
            return !!this[t].removeChild(e[t]);
        }
        inject(e) {
            if (e instanceof Element == 0 || s.test(e.tagName) || n.test(e.innerHTML)) throw new Error("ensemble.Compo error: The remote object could not be resolved into a valid node.");
            return this.empty(), !!this[this._ns].appendChild(e);
        }
        empty() {
            for (; this.first; ) this.remove(this.first);
        }
        get children() {
            return Array.prototype.map.call(this[this._ns].children, (e) => e.__compo);
        }
        get first() {
            const e = this._ns;
            return this[e].firstElementChild ? this[e].firstElementChild.__compo : null;
        }
        get last() {
            const e = this._ns;
            return this[e].lastElementChild ? this[e].lastElementChild.__compo : null;
        }
    } {
        constructor(e, t, s, n, r, a) {
            if (!new.target) throw "ensemble.Compo error: Bad invocation, must be called with new.";
            super();
            const l = (this._ns = "_" + e),
                c = t ? t.toString() : "div";
            if (i.test(t)) throw new Error(`ensemble.Compo error: The tag name provided ('${c}') is not a valid name.`);
            const h = (this[l] = this._element(e, c, s, n, r, a));
            if (((this.__Compo = !0), (this[l].__compo = this), n && "object" == typeof n))
                for (const t in n) {
                    const s = t.toString();
                    if (o.test(s)) throw new Error(`ensemble.Compo error: The property name provided ('${s}') is not a valid name.`);
                    if (0 === s.indexOf("on") && n[s] && "function" == typeof n[s]) h[s] = n[s].bind(this);
                    else if ("object" != typeof n[s]) h[s] = n[s];
                    else if ("children" == s && "object" == typeof n[s] && n[s].length)
                        for (const t of n.children) {
                            const s = t.tag,
                                n = t.name,
                                i = t.props;
                            this.append(new Compo(e, s, n, i));
                        }
                }
            if (s) {
                const t = h.className;
                (h.className = ""), "string" == typeof s ? (h.className = e + "-" + s) : "object" == typeof s && (h.className = s.map((t) => e + "-" + t).join(" ")), t && (h.className += " " + t);
            }
            this._renderer();
        }
        _element(e, t, s, n, i, o) {
            return o ? document.createElementNS(t, [...o, ...i]) : document.createElement(t, i);
        }
        hasAttr(e) {
            return this[this._ns].hasAttribute(e);
        }
        getAttr(e) {
            return this[this._ns].getAttribute(e);
        }
        setAttr(e, t) {
            this[this._ns].setAttribute(e, t);
        }
        delAttr(e) {
            this[this._ns].removeAttribute(e);
        }
        getStyle(e) {
            return window.getComputedStyle(this[this._ns])[e];
        }
        show() {
            this[this._ns].hidden = !1;
        }
        hide() {
            this[this._ns].hidden = !0;
        }
        enable() {
            this[this._ns].disabled = !1;
        }
        disable() {
            this[this._ns].disabled = !0;
        }
        get node() {
            return console.warn("ensemble.Compo", "Direct access to the node is strongly discouraged."), this[this._ns];
        }
        get parent() {
            const e = this._ns;
            return this[e].parentElement && "__compo" in this[e].parentElement ? this[e].parentElement.__compo : null;
        }
        get previous() {
            const e = this._ns;
            return this[e].previousElementSibling ? this[e].previousElementSibling.__compo : null;
        }
        get next() {
            const e = this._ns;
            return this[e].nextElementSibling ? this[e].nextElementSibling.__compo : null;
        }
        get classList() {
            return this[this._ns].classList;
        }
        static isCompo(e) {
            return t ? t.for(e) === t.for(Compo.prototype) : e && "object" == typeof e && "__Compo" in e;
        }
        get [t.toStringTag]() {
            return "ensemble.Compo";
        }
    }
    class Data {
        constructor(e, t) {
            if (!new.target) throw "ensemble.Data error: Bad invocation, must be called with new.";
            t && "object" == typeof t && Object.assign(this, {}, t);
            const s = (this._ns = "_" + e);
            (this.__Data = !0), (this[s] = { ns: e });
        }
        compo(e, t, s, n = !1, i = !1, o = !1) {
            const r = this[this._ns].ns;
            let a;
            return (a = n ? { ns: r, tag: e, name: t, props: s, fresh: i, stale: o } : new Compo(r, e, t, s)), i && "function" == typeof i && (a.fresh = s.onfresh = i), o && "function" == typeof o && (a.stale = s.onstale = o), a;
        }
        async render(e) {
            const t = this._ns;
            (this[t][e] && this[t][e].rendered) || ((this[t][e] = { rendered: !0, fresh: this[e].fresh, stale: this[e].stale, params: this[e] }), (this[e] = new Compo(this[e].ns, this[e].tag, this[e].name, this[e].props))),
                this[t][e].fresh();
        }
        async stale(e) {
            const t = this._ns;
            this[t][e] && this[t][e].rendered && this[t][e].stale();
        }
        async reflow(e, t) {
            const s = this._ns;
            t ? (this[s][e] = this.compo(this[s][e].params.ns, this[s][e].params.name, this[s][e].params.props)) : this[s][e] && this[s][e].rendered && this[s][e].fresh();
        }
        static isData(e) {
            return t ? t.for(e) === t.for(Data.prototype) : e && "object" == typeof e && "__Data" in e;
        }
        get [t.toStringTag]() {
            return "ensemble.Data";
        }
    }
    class Event {
        constructor(e, t, s) {
            if (!new.target) throw "ensemble.Event error: Bad invocation, must be called with new.";
            const n = (this._ns = "_" + e);
            (s = (Compo.isCompo(s) ? s.node : s) || document), (this.__Event = !0), (this[n] = { name: t, node: s });
        }
        add(e, t = !1) {
            this[this._ns].node.addEventListener(this[this._ns].name, e, t);
        }
        remove(e) {
            this[this._ns].node.removeEventListener(this[this._ns].name, e);
        }
        static isEvent(e) {
            return t ? t.for(e) === t.for(Event.prototype) : e && "object" == typeof e && "__Event" in e;
        }
        get [t.toStringTag]() {
            return "ensemble.Event";
        }
    }
    e.SocialShare = class SocialShare extends class base {
        constructor() {
            const e = "ensemble" + (new.target && new.target.name ? "." + new.target.name : "");
            let t, s;
            if ((arguments.length > 1 ? ((t = arguments[0]), (s = arguments[1])) : (s = arguments[0]), s && "object" != typeof s)) throw new TypeError(`${e} error: The passed argument 'options' is not of type Object.`);
            if (t && "object" != typeof t) throw new TypeError(`${e} error: The passed argument 'element' is not of type Object.`);
            this._bindings(), (this.options = this.defaults(this._defaults(), s)), Object.freeze(this.options), (this.element = t);
        }
        defaults(e, t) {
            const s = {};
            for (const n in e) null != e[n] && "object" == typeof e[n] ? (s[n] = Object.assign(e[n], t[n])) : (s[n] = void 0 !== t[n] ? t[n] : e[n]);
            return s;
        }
        compo(e, t, s) {
            return null != e ? new Compo(this.options.ns, e, t, s) : Compo;
        }
        data(e) {
            return null != e ? new Data(this.options.ns, e) : Data;
        }
        event(e, t) {
            return "string" == typeof e ? new Event(this.options.ns, e, t) : e ? (e.preventDefault(), void e.target.blur()) : Event;
        }
        selector(e, t, s = !1) {
            return (t = t || document), s ? t.querySelectorAll(e) : t.querySelector(e);
        }
        appendNode(e, t) {
            return !!e.appendChild(t);
        }
        prependNode(e, t) {
            return !!e.prependChild(t);
        }
        removeNode(e, t) {
            return !!e.removeChild(t);
        }
        cloneNode(e, t = !1) {
            return e.cloneNode(t);
        }
        hasAttr(e, t) {
            return e.hasAttribute(t);
        }
        getAttr(e, t) {
            return e.getAttribute(t);
        }
        setAttr(e, t, s) {
            e.setAttribute(t, s);
        }
        delAttr(e, t) {
            e.removeAttribute(t);
        }
        binds(e) {
            const t = this;
            return function (s) {
                e.call(t, s, this);
            };
        }
        delay(e, t, s) {
            const n = t ? this.timing(t) : 0;
            setTimeout(e, n || s);
        }
        timing(e, t = "transitionDuration") {
            let s = Compo.isCompo(e) ? e.getStyle(t) : window.getComputedStyle(e)[t];
            return s && (s = s.indexOf("s") ? 1e3 * parseFloat(s) : parseInt(s)), s || 0;
        }
    } {
        _defaults() {
            return {
                ns: "share",
                fx: !0,
                root: "body",
                className: "social-share",
                link: "",
                title: "",
                description: "",
                displays: null,
                intents: { facebook: 0, twitter: 0, whatsapp: 1, linkedin: 0, "copy-link": 3},
                uriform: {
                    facebook: "https://facebook.com/sharer.php?u=%url%",
                    twitter: "https://twitter.com/share?url=%url%&text=%title%",
                    whatsapp: "https://api.whatsapp.com/send?text=%text%",
                    linkedin: "https://www.linkedin.com/sharing/share-offsite?mini=true&url=%url%&title=%title%&ro=false&summary=%summary%",
                    "send-email": "mailto:?subject=%subject%&body=%text%",
                },
                selectorLink: { element: 'link[rel="canonical"]', attribute: "href" },
                selectorTitle: null,
                selectorDescription: { element: 'meta[name="description"]', attribute: "content" },
                label: {},
                locale: {
                    label: "Share",
                    share: "Share on %s",
                    send: "Send to %s",
                    subject: "An interesting thing",
                    text: "Hi! There is something may interesting you: %s",
                    email: "Send via email",
                    copy: "Copy link",
                    copied: "Copied link!",
                    whatsapp: "WhatsApp",
                    linkedin: "LinkedIn",
                    "web-share": "Share",
                },
                onInit: function () {},
                onIntent: function () {},
            };
        }
        _bindings() {
            this.intent = this.binds(this.intent);
        }
        constructor() {
            if (!new.target) throw "ensemble.SocialShare error: Bad invocation, must be called with new.";
            super(...arguments), this.init();
        }
        generator() {
            const e = this.options,
                t = (this.share = this.compo(!1, !1, { className: "object" == typeof e.className ? e.className.join(" ") : e.className }));
            if ((t.setAttr("data-social-share", ""), e.label)) {
                const s = this.compo("span", "label", e.label);
                s.classList.add("label"), "innerText" in e.label == 0 && (s.innerText = e.locale.label), t.append(s);
            }
            const s = (this.actions = this.compo("ul", "actions"));
            t.append(s), (this.built = !0);
        }
        init() {
            const e = this.options;
            this.built ||
                ((this.root = this.selector(e.root)),
                (this.displays = e.displays && "object" == typeof e.displays ? e.displays : Object.keys(e.intents)),
                this.generator(),
                this.element &&
                    this.share.up(
                        this.element,
                        function (e) {
                            this.element = e;
                        }.bind(this)
                    ),
                this.populate(),
                e.onInit.call(this, this));
        }
        populate() {
            const e = this.options;
            for (const t in e.intents) {
                if (-1 == this.displays.indexOf(t)) continue;
                const s = t in e.locale ? e.locale[t] : t.replace(/\w/, (e) => e.toUpperCase());
                let n;
                switch (e.intents[t]) {
                    case 0:
                        n = e.locale.share.replace("%s", s);
                        break;
                    case 1:
                        n = e.locale.send.replace("%s", s);
                        break;
                    case 2:
                        n = e.locale.email;
                        break;
                    case 3:
                        n = e.locale.copy;
                        break;
                    case 4:
                        if (!("share" in window.navigator) || "function" != typeof window.navigator.share) continue;
                        n = e.locale["web-share"];
                }
                this.action(t, n);
            }
        }
        action(e, t) {
            const s = this.options,
                n = this.compo("li", "action", { className: s.ns + "-action-" + e }),
                i = this.compo("button", ["button", "intent"], { className: s.ns + "-intent-" + e, title: t, ariaLabel: t, onclick: this.intent });
            n.setAttr("data-share-intent", e), n.append(i);
            const o = this.compo("span", "icon", { className: "icon-" + e });
            i.append(o), this.actions.append(n);
        }
        intent(e, t) {
            if ((this.event(e), !e.isTrusted)) return;
            const s = this.options;
            if (!this.compo().isCompo(t)) return;
            const n = t.parent;
            if (!n || !n.hasAttr("data-share-intent")) return;
            const i = n.getAttr("data-share-intent");
            if (-1 == this.displays.indexOf(i)) return;
            let o, r, a, l;
            (o = s.link ? s.link : s.selectorLink && "object" == typeof s.selectorLink && this.selector(s.selectorLink.element) ? this.getAttr(this.selector(s.selectorLink.element), s.selectorLink.attribute) : window.location.href),
                (r = s.title ? s.title : s.selectorTitle && "object" == typeof s.selectorTitle && this.selector(s.selectorTitle.element) ? this.getAttr(this.selector(s.selectorTitle.element), s.selectorTitle.attribute) : document.title),
                (a = s.description
                    ? s.description
                    : s.selectorDescription && "object" == typeof s.selectorDescription && this.selector(s.selectorDescription.element)
                    ? this.getAttr(this.selector(s.selectorDescription.element), s.selectorDescription.attribute)
                    : r),
                (l = "\r\n\r\n%title%\r\n%url%\r\n\r\n");
            const c = { url: o, title: r, text: "\r\n\r\n%title%\r\n%url%\r\n\r\n", summary: a };
            if ((s.onIntent.call(this, this, e, i, c), (c.text = s.locale.text.replace("%s", c.text)), i in s.intents))
                switch (i) {
                    case "send-email":
                        this.sendEmail(e, c);
                        break;
                    case "copy-link":
                        this.copyLink(e, c);
                        break;
                    case "web-share":
                        this.webShare(e, c);
                        break;
                    default:
                        this.social(e, c, i, n);
                }
        }
        text(e) {
            return encodeURIComponent(e.text.replace("%url%", e.url).replace("%title%", e.title).replace("%summary%", e.summary));
        }
        social(e, t, s, n) {
            const i = this.options;
            if (s in i.uriform == 0) return;
            let o = i.uriform[s].replace("%url%", encodeURIComponent(t.url)).replace("%title%", encodeURIComponent(t.title)).replace("%summary%", encodeURIComponent(t.summary));
            const r = n.getAttr("ariaLabel"),
                a = "toolbar=0,status=0,width=640,height=480";
            if ((/%text%/.test(i.uriform[s]) && (o = o.replace("%text%", this.text(t))), "messenger" == s)) {
                const e = "messenger_app_id" in i ? i.messenger_app_id : "";
                o = o.replace("%app_id%", encodeURIComponent(e));
            }
            console.log(o, r, a), window.open(o, r, a);
        }
        sendEmail(e, t) {
            const s = this.options,
                n = s.uriform["send-email"].replace("%subject%", encodeURIComponent(s.locale.subject)).replace("%text%", this.text(t));
            console.log(n, "_self"), window.open(n, "_self");
        }
        copyLink(e, t) {
            if (!this.element) return;
            const s = this.options,
                n = document.createElement("textarea");
            if (
                ((n.style = "position:absolute;width:0;height:0;opacity:0;z-index:-1;overflow:hidden"), (n.value = t.url.toString()), this.appendNode(this.element, n), n.focus(), n.select(), document.execCommand("copy"), n.remove(), s.fx)
            ) {
                const e = this.root,
                    t = this.compo(!1, "fx-copied-link--ground", { hidden: !0 }),
                    n = this.compo("span", "copied-link-message", { innerText: s.locale.copied });
                e.classList.add("share-fx-copied-link"),
                    t.install(e),
                    n.install(e),
                    t.show(),
                    this.delay(
                        function () {
                            n.uninstall(e), t.uninstall(e), e.classList.remove("share-fx-copied-link");
                        },
                        t,
                        800
                    );
            }
        }
        async webShare(e, t) {
            try {
                await window.navigator.share({ title: t.title, url: t.url });
            } catch (e) {
                e instanceof TypeError ? console.info("ensemble.SocialShare.webShare", "TODO fallback") : console.log("ensemble.SocialShare.webShare", e.message);
            }
        }
    };
});
