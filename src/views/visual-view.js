import { html } from 'lit-element';
import { BaseView } from './base-view.js';
import { visualViewCss } from './visual-view-css';
import '@polymer/iron-ajax/iron-ajax.js';
import '@google-web-components/google-chart/google-chart.js';

class VisualView extends BaseView {
  static get properties() {
    return {
      viewData: { type: String },
      labels: { type: Object },
      colors: { type: Array },
      options: { type: Object }
    };
  }

  constructor() {
    super();
    this.viewData = '';
    this.labels = {
              "1 dn": "Digha Nikaya",
              "2 mn": "Majjhima Nikaya",
              "3 sn": "Samyutta Nikaya",
              "4 an": "Anguttara Nikaya",
              "an": "Anguttara Nikāya",
              "arv": "Arthaviniścaya",
              "avs": "Avadānaśataka",
              "bv": "Buddhavaṃsa",
              "cnd": "Cūḷaniddesa",
              "cp": "Cariyāpiṭaka",
              "d": "Tibetan Suttas",
              "da": "Dīrghāgama",
              "dhp": "Dhammapada",
              "divy": "Divyāvadāna",
              "dn": "Digha Nikāya",
              "ds": "Dhammasaṅgaṇī",
              "ea": "Ekottarikāgama",
              "g": "Gāndhārī Dharmapada 3",
              "gdhp": "Gāndhārī Dharmapada",
              "gf": "Gāndhārī fragments",
              "iti": "Itivuttaka",
              "ja": "Jātaka",
              "kf": "Khotanese fragments",
              "kp": "Khuddakapāṭha",
              "kv": "Kathāvatthu",
              "lal": "Lalitavistara",
              "lzh": "Chinese Vinaya",
              "ma": "Madhyamāgama",
              "mil": "Milindapañha",
              "mn": "Majjhima Nikāya",
              "mnd": "Mahāniddesa",
              "ne": "Netti",
              "pdhp": "Patna Dharmapada",
              "pe": "Peṭakopadesa",
              "pf": "Prākrit fragments",
              "pli": "Pali Vinaya",
              "pp": "Puggalapaññatti",
              "ps": "Paṭisambhidāmagga",
              "pv": "Petavatthu",
              "sa": "Saṃyuktāgama",
              "sag": "Śarīrārthagāthā",
              "san": "Sanskrit Vinaya",
              "sf": "Sanskrit Fragments",
              "sht": "SHT fragments",
              "sn": "Samyutta Nikāya",
              "snp": "Suttanipāta",
              "t": "Chinese Suttas",
              "thi": "Therīapadāna",
              "tha": "Therāpadāna",
              "thag": "Theragāthā",
              "thig": "Therīgāthā",
              "ud": "Udāna",
              "uf": "Uighur fragments",
              "up": "Upāyikā",
              "uv": "Udānavarga",
              "uvs": "Udānavarga de Subaši",
              "vb": "Vibhaṅga",
              "vv": "Vimānavatthu",
              "other": "Other"};
  this.colors = ['rgb(23, 190, 207)',
                'rgb(31, 119, 180)',
                'rgb(255,127,14)',
                'rgb(44, 160, 44)',
                'rgb(214, 39, 40)',
                'rgb(148, 103, 189)',
                'rgb(140, 86, 75)',
                'rgb(227, 119, 194)',
                'rgb(127, 127, 127)',
                'rgb(188,189,34)',
                'rgb(23, 190, 207)',
                'rgb(44, 160, 44)',
                'rgb(255,127,14)',
                'rgb(44, 160, 44)',
                'rgb(214, 39, 40)',
                'rgb(148, 103, 189)',
                'rgb(140, 86, 75)',
                'rgb(255,127,14)',
                'rgb(31, 119, 180)',
                'rgb(188,189,34)',
                'rgb(23, 190, 207)',
                'rgb(148, 103, 189)',
                'rgb(227, 119, 194)',
                'rgb(140, 86, 75)',
                'rgb(214, 39, 40)',
                'rgb(227, 119, 194)',
                'rgb(44, 160, 44)',
                'rgb(127, 127, 127)',
                'rgb(23, 190, 207)'];
  this.options = {
                sankey: {
                    iterations: 0,
                    node: {
                      width: 40,
                      interactivity: true,
                      colors: this.colors,
                      label: { 
                            fontSize: 14,
                            bold: true
                      }
                    },
                    link: {
                      colorMode: 'gradient',
                      fillOpacity: 0.4,
                      colors: this.colors
                    }
                }
              };
  }

  render() {
    return html`
      ${visualViewCss}

      <p class="expanation-text">Click on any collection on the left side in the chart to open it.</p>
      <button @click="${this.loadData}">Click here to load data</button>
      <google-chart
          id="parallels-chart"
          type="sankey"
          @google-chart-select="${this.selectSubCollection}">
      </google-chart>
    `;
  }

  loadData() {
    this.drawChart(`./pali-parallels/suttas.json`);
  }

  drawChart(url) {
    let windowHeight = window.innerHeight-200;
    let windowWidth = window.innerWidth-30;
    let chart = this.querySelector('#parallels-chart');
    chart.style.width = windowWidth + 'px';
    fetch(url).then(r => r.json()).then(sankey_data => {
      for (let i = 0; i < sankey_data.length; i++) {
        sankey_data[i][0] = `${sankey_data[i][0]}`;
        sankey_data[i][1] = `${sankey_data[i][1]}`;
        if (this.labels[sankey_data[i][0]]) {
          sankey_data[i][0] = `${sankey_data[i][0]} ${this.labels[sankey_data[i][0]]}`;
        };
        if (this.labels[sankey_data[i][1].slice(3,)]) {
          sankey_data[i][1] = `${this.labels[sankey_data[i][1].slice(3,)]}`;
        };
      }

      let data = new google.visualization.DataTable();
      data.addColumn('string', 'From');
      data.addColumn('string', 'To');
      data.addColumn('number', 'Nr. of parallels');
      data.addRows(sankey_data);
      chart.data = data;
      chart.options = this.options;
      chart.style.height = ((sankey_data.length * 4) > windowHeight) ? `${sankey_data.length * 4}px` : `${windowHeight-100}px`;
    });
  }

  selectSubCollection(e) {
    let targetName = e.detail.chart.getSelection()[0].name.split(' ')[1];
    let url = `./pali-parallels/${targetName}.json`;
    (url) ? this.drawChart(url) : '';
  }

}

customElements.define('visual-view', VisualView);
