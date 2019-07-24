import { LitElement, html } from 'lit-element';

export const visualViewCss =  html`
<style>
    p.expanation-text {
    	text-align: center;
    }

    .catTitle{font-weight:bold;color:blue;}
    .trgTxt{font-weight:bold;color:red;}
    .myPosition{position:fixed;}
    .quotedText{font-weight:bold;}
    .mText{padding:10px;margin:10px}
    .activeText{a:hover {text-decoration: underline}};
    .sktsource{background:white;}
    .sktsource:hover{background:silver;transition: background-color 500ms linear;}
    .tibsource{background:white;}
    .tibsource:hover{background:silver;transition: background-color 500ms linear;}
    .transHighlight{background:silver;transition: background-color 500ms linear;}

    #parallels-chart {
      font: 13px sans-serif;
      padding: 30px;
    }

    .node rect {
      fill-opacity: .9;
      shape-rendering: crispEdges;
      stroke-width: 0;
    }

    .node text {
      text-shadow: 0 1px 0 #fff;
    }

    .link {
      fill: none;
      stroke: #000;
      stroke-opacity: .2;
    }

    .loadJson,.matchedText {
      cursor:pointer;color:blue;
    }

    .full{height:100%}

    .loadJson:hover{font-weight:bold;color:red;}
    #mainDialog{height:0px;width:100%;bottom:0px}
    #sanskritDialog{height:0px;width:100%;bottom:0px}
    #subDialog{height:0px;width:100%;bottom:0px}

</style>`;