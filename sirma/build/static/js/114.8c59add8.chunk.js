"use strict";(self.webpackChunkmy_react_components=self.webpackChunkmy_react_components||[]).push([[114],{8161:function(t,e,a){a(2791),a(4277)},6114:function(t,e,a){a.r(e),a.d(e,{default:function(){return l}});var n=a(9439),c=a(2791),o=a(1243),s=a(4925),u=a(4277),r=(a(8161),a(184)),i=c.lazy((function(){return Promise.all([a.e(16),a.e(74)]).then(a.bind(a,9074))}));function l(){var t=(0,c.useState)([]),e=(0,n.Z)(t,2),a=e[0],l=e[1],h=(0,c.useState)([]),f=(0,n.Z)(h,2),m=f[0],p=f[1],d=(0,c.useState)([]),g=(0,n.Z)(d,2),v=g[0],Z=g[1],y=(0,c.useState)([]),S=(0,n.Z)(y,2),b=S[0],x=S[1],w=(0,c.useState)(!0),T=(0,n.Z)(w,2),_=(T[0],T[1]),j=(0,s.s0)(),k=(0,u.v9)((function(t){return t.user.access})),z=localStorage.getItem("img");return(0,c.useEffect)((function(){var t=localStorage.getItem("url");null===t&&j("/auth/company");var e=t+"api/companies/";o.Z.get(e,{headers:{Authorization:"JWT ".concat(k)}}).then((function(t){l(t.data.results||[])})).catch((function(t){console.log(t)}));var a=t+"api/companies/contact_result";o.Z.get(a,{headers:{Authorization:"JWT ".concat(k)}}).then((function(t){x(t.data.results||[])})).catch((function(t){console.log(t)}));var n=t+"api/companies/country";o.Z.get(n,{headers:{Authorization:"JWT ".concat(k)}}).then((function(t){p(t.data.results||[])})).catch((function(t){console.log(t)}));var c=t+"api/companies/contact_type";o.Z.get(c,{headers:{Authorization:"JWT ".concat(k)}}).then((function(t){Z(t.data.results||[])})).catch((function(t){console.log(t)})),_(!1)}),[]),(0,r.jsx)(c.Suspense,{fallback:(0,r.jsx)("div",{className:" w-[100%] h-[700px] flex flex-column justify-center  items-center ",children:(0,r.jsx)("img",{className:"  w-[50%] m-auto  p-20 shadow-sm shadow-blue-100",src:z})}),children:(0,r.jsx)(i,{tableData:a,setTableData:l,states:m,contactType:v,contactResult:b})})}}}]);
//# sourceMappingURL=114.8c59add8.chunk.js.map