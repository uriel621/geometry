import React from 'react';
//import 'semantic-ui-css/semantic.min.css'; // in index.html
// import { Select } from 'semantic-ui-css'
const calculator_div_style = {
    'maxWidth':'560px', 
    'height':'360px', 
    'border':'1px solid rgb(39, 145, 218)',
    'margin':'0 auto',
    'textAlign':'center',
}

const select_shape_style = {
    'float':'left',
    'width':'49.5%',
    'border': '1px solid #bfdcf0'
}

const select_formula_style = {
    'float':'right',
    'width':'49.5%',
    'border': '1px solid #bfdcf0'
}

const clearfix = {
    'clear':'both'
}

const image_formula_div_style = {
    'height':'70px',
    'verticalAlign': 'middle',
    'lineHeight': '70px',
    // 'border': 'solid 0.5px'
}

const image_formula = {
    // 'width':'78px', 
    // 'height':'22px'
}

const details_div_style = {
    'height':'220px'
}

const image_shape_div = {
    'float':'left',
    // 'border': 'solid 0.5px',
    'width':'50%',
    'height':'100%',
    'verticalAlign': 'middle',
    'lineHeight': '220px'
}

const image_shape = {
    'maxHeight': '95%',
    'maxWidth': '95%'
}

const input_data = {
    'float':'right',
    // 'border': 'solid 0.5px',
    'width':'50%',
    'height':'100%',
    'textAlign':'left'
    // 'verticalAlign': 'middle',
    // 'lineHeight': '155px'
}

const input_div = {
    // 'textAlign':'left'
}

const result_label = {
    // marginTop: '10%',
    // marginBottom: '10%',
    // textAlign: 'center'
}

const input_css = {
    fontSize: '13px',
    width: '100%',
    color: '#555',
    backgroundColor: '#f2f8fc',
    border: '1px solid #bfdcf0',
    padding: '1px 1px',
    textAlign: 'center',
}

const Inputs = (props) => {
    console.log('lolololol', props)
    return(
        <div>
            {
                props.values.map( (value, index) => {
                    let width = '49%';
                    if(props.values.length === 1 || props.values.length === 2) {
                        width = '99%';
                    }
                    let style = { 'display':'inline-block', 'marginTop':'2.5%', 'marginLeft':'0.5%', 'marginRight':'0.5%', 'width': width }
                    let label_name = value[0].toUpperCase() + value.slice(1);
                    let replace = label_name.replace('_', ' ');
                    let _index = replace.indexOf(' ');
                    let letter = label_name.substring(_index+1)
                        label_name = label_name.substring(0, _index)
                        label_name = `${label_name} (${letter})`;
                    let div =   <div key={ index } style={ style }>
                                    <label className="label" style={{ "textAlign":"left" }} >{ label_name }: </label>
                                    <input style={ input_css } type='number' id={ value }  className='input' onKeyUp={ props.method } />
                                </div> 
                    return div     
                })
            }
        </div>
    )
}


const Select = (props) => {
    if(!props.options){
        return (
            <div></div>
        )
    }
    return (
        <select className="select" style={ props.style } onChange={ props.method }>
            {
                props.options.map((option, index) => {
                    
                    let section_text = option[0].toUpperCase() + option.slice(1);
                        section_text = section_text.replace('_', ' ')
                        // cut the the word capital then join them
                    let _index = section_text.indexOf(' ')
                    if(_index !== -1){
                        section_text[_index + 1].toUpperCase()
                    }
                    // console.log(section_text)
                    // let section_text = option.replace('_', ' ')
                    // let _index = _section_text.indexOf(' ')
                    // console.log(_section_text)
                    // console.log(_index)

                    // if(_index !== -1){
                    //     console.log(section_text[_index + 1].toUpperCase() + option)
                    // }
                    // let section_text = option[0].toUpperCase() + option.slice(1);
                    if(index === 0){
                        option = <option key={ index } value={ option } defaultValue>{ section_text }</option>;
                    }
                    else{
                        option = <option key={ index } value={ option }>{ section_text }</option>;
                    }
                    return option
                })          
            }
        </select>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);

        this.data = null;
        fetch('/static/shapes.json')
            .then(response => response.json())
            .then(data => {
                this.data = data
                this.select()
            })      

        this.state = {
            all_shapes: null,
            formulas_for_shapes: ["area", "circumference", "diameter", "radius"],
            current_shape: 'circle',
            current_formula: 'area',
            needed_values: ["radius_r"],
            image_formula: 'static/images/formula_images/circle/area.png',
            image_shape: 'static/images/shape_images/circle.png',
            answer: '?'
        } 

        this.input_calculate = this.input_calculate.bind(this);
        this.select = this.select.bind(this);
        this.find_formulas = this.find_formulas.bind(this);
        this.calculate = this.calculate.bind(this);
        this.image_formula = this.image_formula.bind(this);
        this.image_shape = this.image_shape.bind(this);
        this.answer = this.answer.bind(this);
    }

    select(){
        let options = [];
        Object.keys(this.data).forEach(key => {
            options.push(key);
        })
        this.setState({ 'all_shapes': options })
        this.setState({ 'answer': '?' })
        document.querySelectorAll('input').forEach(input => input.value = '');        
    }

    find_formulas(event){
        var formula_select_element = event.target.parentNode.children[1]
            formula_select_element.selectedIndex = 0;
        let shape = event.target.value;
        let formulas = [];  
        Object.keys(this.data).forEach(key => {
            if(shape === key) {
                Object.keys(this.data[key]).forEach(key => {
                    formulas.push(key)
                })
                this.setState({ 'formulas_for_shapes': formulas })
                this.setState({ 'current_shape': shape })
                this.setState({ 'current_formula': formulas[0] })
                
                this.input_calculate(false, formulas[0], shape)
                this.image_formula(shape, formulas[0])
                this.image_shape(shape)
            }
        })
    }

    input_calculate(event, auto, _shape){
        let shape = null;
        let formula = null;
        if(!event){
            formula = auto;
            shape = _shape;
        }
        else {
            shape = this.state.current_shape;
            formula = event.target.value;
        }                                      
        Object.keys(this.data).forEach(key => {
            if(shape === key){
                var response = this.data[key];
                Object.keys(response).forEach(key => {
                    if(formula === key) {
                        this.setState({ 'current_formula':formula })
                        this.setState({ 'needed_values':  response[key] })
                        this.setState({ 'answer': '?' })
                        document.querySelectorAll('input').forEach(input => input.value = '');
                        this.image_formula(shape, formula)
                    }
                })
            }
        });
    }

    calculate(event){
        // console.log(event.target.id);
        // console.log(event.target.value);
        // console.log(this.state.current_shape);
        // console.log(this.state.current_formula);
        // console.log(this.state.needed_values.length);

        var form_data = new FormData()
            form_data.append("shape", this.state.current_shape);
            form_data.append("formula", this.state.current_formula);

            let some  = [];
            this.state.needed_values.forEach((value, index) => {
                var input_values = document.querySelector(`#${ value }`).value;
                if(!input_values){
                    return
                }
                console.log(value, '-->', input_values)
                    input_values = [value, input_values]
                    some.push(input_values)
            })
        form_data.append("needed_values", some)
        if(this.state.needed_values.length === some.length){
        console.log(event.target)
            
            // console.log('some: ', some)
            // console.log(...form_data)
            // let data = {
            //     "shape": this.state.current_shape,
            //     "formula": this.state.current_formula,
            //     "needed_values": some,
            // }
            
            const request = new XMLHttpRequest();
                request.open('POST', '/calculate', true);
                request.send(form_data)
                request.onload = this.answer  
        }
        else {
            this.setState({ 'answer': '?' })
        }

    }

    image_shape(shape){
        const src = `static/images/shape_images/${shape}.png`
        this.setState({ "image_shape":src });
    }

    image_formula(shape, formula){
        const src = `static/images/formula_images/${shape}/${formula}.png`
        this.setState({ "image_formula":src });
    }

    answer(request){
        let data = JSON.parse(request.currentTarget.response)
        this.setState({ 'answer':data })
    }

    render(){
        console.log(this.state)
        return (
            <div>
                <div style={ calculator_div_style }>
                    <div>
                        <h1 className="title is-3">Geometry Calculator</h1>
                    </div>
                    <div>
                        <Select style={ select_shape_style } options={ this.state.all_shapes } method={ this.find_formulas }/>
                        <Select style={ select_formula_style } options={ this.state.formulas_for_shapes } method={ this.input_calculate }/>
                        <div style={ clearfix }></div>
                    </div>
                    <div style={ image_formula_div_style }>
                        <img style={ image_formula }src={ this.state.image_formula } />
                        {/* <img style={ image_formula }src="https://i.ytimg.com/vi/riNAA-jx0u8/maxresdefault.jpg" /> */}
                    </div>
                    <div style={ details_div_style }>
                        <div style={ image_shape_div } >
                            <img style={ image_shape } src={ this.state.image_shape } />
                            {/* <img style={ image_shape } src="http://store-images.s-microsoft.com/image/apps.26251.13510798883213349.c74c048e-8bf5-42b5-9825-57104efe5ff6.058ff6e5-b6b5-4bd6-9fcc-4fda6bc214ec?w=180&h=180&q=60" /> */}
                        </div>
                        <div style={ input_data } >
                            <label className="label" style = { result_label }>{ this.state.current_formula }: { this.state.answer }</label>
                            {/* <div>{ 'Area' }: {'?'}</div> */}
                            <div style={{ 'textAlign':'center', 'marginTop':'8%', 'marginBottom':'8%' }}>
                                {/* { inputs(["radius"]) }  */}
                                <Inputs values={ this.state.needed_values } method={ this.calculate }/>
                            </div>
                        </div>
                        <div style={ clearfix }></div>
                    </div>
                </div>
            </div>
        )
    }
}
// request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')


        // $.ajax({
        //     url: '/static/shapes.json',
                // type:'POST',
                // data: formdata: false,
                // proccessData:false,
                // contentType:false
        //     success: this.calculate_success
        // })


        //     // const request = new XMLHttpRequest();
//     // request.open('post', url, true);

//     // request.onload = function() {
//     //     if(request.status >= 200 && request.status < 400) {
//     //         console.log(request);
//     //         var response = request.response;
//     //         console.log('SUCCESS: ', response);
//     //     }
//     //     else {
//     //         console.log('Target reached but error');
//     //     }
//     // }
    
//     // request.onerror = function() {
//     //     console.log('ERROR')
//     // }
//     // request.send();

// fetch('/static/shapes.json')
//     .then(response => response.json())
//     .then(data => console.log(data))
export default App;