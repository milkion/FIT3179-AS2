var vg_1 = "drug-addicts-in-malaysia.vg.json";
var vg_2 = "drug-types.vg.json";

vegaEmbed('#map_chart', vg_1).then(function(result) {}).catch(console.error);
vegaEmbed('#bar_chart', vg_2).then(function(result) {}).catch(console.error);