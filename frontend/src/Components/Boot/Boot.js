import React from 'react'
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
import Button from '@mui/material/Button';
import MicIcon from '@mui/icons-material/Mic';
import PauseIcon from '@mui/icons-material/Pause';
import Stack from '@mui/material/Stack';
import './Boot.css';

let reader;

class Boot  extends React.Component {
  constructor(props) {
    super(props)
 
    this.state = {
      recordState: null,
      message:'',
      answer:'',
      c:false,
      speak:false
    }
    this.fetchChat = this.fetchChat.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.start = this.start.bind(this)
    this.stop = this.stop.bind(this)
    //this.onstop = this.onstop.bind(this)
    this.sub = React.createRef()
    this.child = React.createRef();
    this.button = React.createRef();




  }

 
  componentDidMount(){
    this.fetchChat()

 
  }
componentDidUpdate(pp,ps,ss){
  if(ps.answer!=this.state.answer)
  this.button.current.click()
}
 
  fetchChat(){
    
    
    console.log('Fetching...')
    fetch('http://127.0.0.1:8000/Home/api/chat/')
    .then(response=>response.json())
    .then(data => 
      this.setState({message:data},
        console.log(data))
      
      )
  }

  handleSubmit(e){
    
    
    this.fetchChat()

    e.preventDefault()
    
    console.log('ITEM:', this.state.message)
    

    var url = 'http://127.0.0.1:8000/Home/api/chat-create/'

    fetch(url, {
      method:'POST',
      headers:{
        'Content-type':'application/json',
      },
      body:JSON.stringify(this.state.message)
      
    }).then((response)  => {
        let r=response.json()

        r.then(data=> 
          this.setState({answer:data}),
          console.log('answer', this.state.answer),


        )
        this.fetchChat()
        this.setState({
          message:''
       })
       this.setState({ speak:true});

        
       //this.button.current.click()

    }).catch(function(error){
      console.log('ERROR:', error)
    })

  }
 
  start = () => {
    this.setState({
      recordState: RecordState.START
    })
  }
 
  stop = () => {
    this.setState({
      recordState: RecordState.STOP,
    })
    
    //this.setState({ speak:true});
    
    

  }
  
 
  //audioData contains blob and blobUrl
  onStop = (audioData) => {
    console.log('audioData', audioData)

    var recordedBlob =audioData.blob
      console.log(recordedBlob)

     reader = new FileReader();
      reader.readAsDataURL(recordedBlob); 
      var that=this 
      console.log(reader.result)
      reader.onloadend = (e)=> {
        var base64data = reader.result;
        console.log(typeof(base64data))
        that.setState({ message: base64data , c:true});
        if(this.state.c){
            this.sub.current.click()
            this.setState({ c:false});
            //this.button.current.click();
        }
        
      //this.setState({ speak:true});

        
        //this.fetchChat()
        console.log(base64data)

     }
     //this.handleSubmit()
     console.log('Hhhhh')

  }

  
 

   
 
  render() {
    const data = this.state.answer;

    const { recordState } = this.state
    const that=this
    const speak = (string) => {
      const u = new SpeechSynthesisUtterance();
      const allVoices = speechSynthesis.getVoices();
      u.voice = allVoices.filter(voice => voice.name === "Alex")[0];
      u.text = string;
      u.lang = "en-US";
      u.volume = 1;
      u.rate = 1;
      u.pitch = 1;
      speechSynthesis.speak(u);
      that.setState({ speak: true});
      

  }
    return (
      <div >
    <form  onSubmit={this.handleSubmit}>  
        <button style={{display: 'none'}} ref={this.sub}></button>
    </form>

    <AudioReactRecorder 
    state={recordState} 
    onStop={this.onStop}
    
    />
            {console.log(data)}


    
 
    <Stack  id='btn' direction="row" spacing={2}>
      <Button onClick={this.start} variant="contained" startIcon={<MicIcon />}>
        Start
      </Button>
      <Button  onClick={this.stop} variant="contained" startIcon={<PauseIcon />}>
        Pause
      </Button>
    </Stack>
    
    
    <button style={{display: 'none'}} ref={this.button} onClick={() => speak(data)}>Speak</button>

    
      </div>
    )
  }
}

export default Boot;

