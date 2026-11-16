// Run with macOS JavaScript for Automation when Node is unavailable.
var host = Application.currentApplication();host.includeStandardAdditions = true;
var root='/Users/lzj/vibegame/100daf-tmp2/showcase-site/dist/';
ObjC.import('Foundation');
function readUTF8(path){return ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError(path,$.NSUTF8StringEncoding,null));}
var data=readUTF8(root+'data.js');
var source=readUTF8(root+'app.js');
function assert(value,message){if(!value)throw new Error(message);}
function makeNode(){return {value:'',dataset:{},html:'',listeners:{},classList:{add:function(){},toggle:function(){}},setAttribute:function(){},addEventListener:function(n,f){this.listeners[n]=f;},focus:function(){},showModal:function(){this.open=true;},close:function(){this.open=false;},set innerHTML(s){this.html=s;var m=s.match(/<option value="([^"]+)"/);if(m)this.value=m[1];},get innerHTML(){return this.html;}};}
var reports=[];
['index.html','energy.html','machining.html','animals.html','melee.html','ranged.html','food.html','equipment.html'].forEach(function(page){
 var nodes={};function node(key){return nodes[key]||(nodes[key]=makeNode());}
 var document={querySelector:node,querySelectorAll:function(){return [];},getElementById:function(id){return node('#'+id);},addEventListener:function(){},body:{style:{}}};
 var window={};new Function('window',data)(window);
 new Function('window','document','location',source)(window,document,{pathname:'/'+page});
 var html=node('#app').innerHTML;
 assert(html.length>1500,page+' rendered');assert(html.indexOf('undefined')<0,page+' has no undefined content');
 if(page!=='index.html'){
  var p=window.DELIVERABLES.filter(function(p){return p.id+'.html'===page;})[0];
  assert(html.indexOf('id="iterations"')>=0,'history section exists');
  assert(node('#version-panel').innerHTML.indexOf(p.latest.toUpperCase())>=0,'latest iteration renders');
  if(p.status!=='review') p.items.forEach(function(item,i){node('#compare-tier').value=String(i);node('#compare-tier').listeners.change();
   var versions=p.versions.filter(function(v){return item.images[v.id];});
   versions.forEach(function(v){node('#compare-from').value=v.id;node('#compare-from').listeners.change();var result=node('#compare-pair').innerHTML;assert(result.indexOf(item.images[v.id])>=0,'comparison contains chosen image');assert(result.indexOf('undefined')<0,'no missing image in comparison');});
  });
  if(p.status==='review'){
   assert(html.indexOf('id="mapping"')>=0,'source mapping exists');
   assert(node('#asset-gallery').innerHTML.indexOf(p.items[0].name)>=0,'first asset displayed');
   node('#asset-search').value=p.items[0].tier;node('#asset-search').listeners.input();
   assert(node('#asset-gallery').innerHTML.indexOf(p.items[0].images[p.latest])>=0,'search finds stable asset ID');
   assert(node('#asset-count').textContent.indexOf('1 /')===0,'search narrows to one item');
   node('#asset-search').value='no-results-xyz';node('#asset-search').listeners.input();
   assert(node('#asset-gallery').innerHTML.indexOf('没有匹配')>=0,'empty state '+page+' actual: '+node('#asset-gallery').innerHTML.slice(0,140));
   node('#asset-search').value='';node('#asset-branch').value=p.items[0].branch;node('#asset-branch').listeners.change();
   assert(node('#asset-gallery').innerHTML.indexOf(p.items[0].images[p.latest])>=0,'branch filter');
  }
  reports.push(page+(p.status==='review'?': mapping, '+p.count+' assets, search, branch filter and empty state passed':': final gallery, history and all '+p.count+' tier/version comparisons passed'));
 }else{assert(html.indexOf('energy.html')>=0&&html.indexOf('machining.html')>=0,'both delivery links');reports.push(page+': overview and delivery routes passed');}
});
reports.join('\n');
