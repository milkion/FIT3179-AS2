var vg_1 = "drug-addicts-in-malaysia.vg.json";
var vg_2 = "drug-types.vg.json";
var vg_3 = "drug-age.vg.json";
var vg_4 = "drug-sex.vg.json";

vegaEmbed('#choropleth_map', vg_1).then(function(result) {}).catch(console.error);
vegaEmbed('#drug_types_chart', vg_2).then(function(result) {}).catch(console.error);
vegaEmbed('#drug_age_chart', vg_3).then(function(result) {}).catch(console.error);
vegaEmbed('#drug_sex_chart', vg_4).then(function(result) {}).catch(console.error);
