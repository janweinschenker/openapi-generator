(window.webpackJsonp=window.webpackJsonp||[]).push([[48],{176:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return a})),n.d(t,"metadata",(function(){return c})),n.d(t,"rightToc",(function(){return p})),n.d(t,"default",(function(){return s}));var r=n(1),o=n(9),i=(n(0),n(320)),a={id:"spec-info",title:"Spec Info"},c={id:"spec-info",title:"Spec Info",description:"## OpenAPI",source:"@site/../docs/specification-info.md",permalink:"/docs/spec-info",editUrl:"https://github.com/OpenAPITools/openapi-generator/edit/master/website/../docs/specification-info.md",lastUpdatedBy:"William Cheng",lastUpdatedAt:1641200738},p=[{value:"OpenAPI",id:"openapi",children:[{value:"2.0",id:"20",children:[]},{value:"3.x",id:"3x",children:[]},{value:"Tags",id:"tags",children:[]}]}],l={rightToc:p};function s(e){var t=e.components,n=Object(o.a)(e,["components"]);return Object(i.b)("wrapper",Object(r.a)({},l,n,{components:t,mdxType:"MDXLayout"}),Object(i.b)("h2",{id:"openapi"},"OpenAPI"),Object(i.b)("h3",{id:"20"},"2.0"),Object(i.b)("h3",{id:"3x"},"3.x"),Object(i.b)("h3",{id:"tags"},"Tags"),Object(i.b)("p",null,"Tags basically group endpoints into the same API class file. For example, an endpoint with the ",Object(i.b)("inlineCode",{parentName:"p"},"store")," tag will be generated in the StoreApi class file in most generators."),Object(i.b)("p",null,"Ref: ",Object(i.b)("a",Object(r.a)({parentName:"p"},{href:"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#tagObject"}),"https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#tagObject")))}s.isMDXComponent=!0},320:function(e,t,n){"use strict";n.d(t,"a",(function(){return u})),n.d(t,"b",(function(){return d}));var r=n(0),o=n.n(r);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function p(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var l=o.a.createContext({}),s=function(e){var t=o.a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):c({},t,{},e)),n},u=function(e){var t=s(e.components);return o.a.createElement(l.Provider,{value:t},e.children)},f={inlineCode:"code",wrapper:function(e){var t=e.children;return o.a.createElement(o.a.Fragment,{},t)}},b=Object(r.forwardRef)((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,a=e.parentName,l=p(e,["components","mdxType","originalType","parentName"]),u=s(n),b=r,d=u["".concat(a,".").concat(b)]||u[b]||f[b]||i;return n?o.a.createElement(d,c({ref:t},l,{components:n})):o.a.createElement(d,c({ref:t},l))}));function d(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,a=new Array(i);a[0]=b;var c={};for(var p in t)hasOwnProperty.call(t,p)&&(c[p]=t[p]);c.originalType=e,c.mdxType="string"==typeof e?e:r,a[1]=c;for(var l=2;l<i;l++)a[l]=n[l];return o.a.createElement.apply(null,a)}return o.a.createElement.apply(null,n)}b.displayName="MDXCreateElement"}}]);