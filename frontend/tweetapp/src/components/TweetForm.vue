
<template>
    <div>
      <form @submit.prevent="onSubmit" class="form-inline">
          <label>Name</label>
          <input v-model="name" id='name' placeholder="Name" required="required">
          <label>Tweet</label>
          <textarea v-model="tweet" placeholder="Write you thoughts" required="required"></textarea>
          &nbsp;&nbsp;<button type="submit">Submit</button>
      </form>
    </div>
    <br><br><br>
    
    <va-table :hover="hover" :size="size" v-if="items.length">
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Tweet</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.id">
            <td>{{item.name}}</td>
            <td>{{item.tweet}}</td>
            <td>{{item.created_at}}</td>
        </tr>
        </tbody>
      </table>
    </va-table>
</template>

<script>
export default {
  name: 'TweetForm',
  created(){
    this.getTweets()
  },
  
  data() {
      return {
        name: '',
        tweet: '',
        items:[]
      }
  },
  methods: {
    onSubmit() {
      if(this.tweet.length > 51){
       alert("Tweet should less then 50 character");
       return;
      
      }

      this.axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      this.axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      this.axios.defaults.xsrfCookieName = "csrftoken";
    
      this.axios.post('http://localhost:8080/api/tweet/',{name: this.name,tweet:this.tweet})
      
      .then(res => {
        this.name = ""
        this.tweet = ""
        this.getTweets()
        console.log(res);
      })
      
      .catch(error => {
        console.log(error)
      })
     
    },
    
    getTweets() {
        this.axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
        this.axios.get('http://localhost:8080/api/tweet/')
        .then(res => {
            this.items = res.data
            console.log(res);
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style >
  table {
    font-family: 'Open Sans', sans-serif;
    width: 750px;
    border-collapse: collapse;
    border: 3px solid #38383b;
    margin: 10px 10px 0 10px;
  }

  table th {
    text-transform: uppercase;
    text-align: left;
    background: #4d4f57;
    color: #FFF;
    padding: 8px;
    min-width: 30px;
  }

  table td {
    text-align: left;
    padding: 8px;
    border-right: 2px solid #707494;
  }
  table td:last-child {
    border-right: none;
  }
  table tbody tr:nth-child(2n) td {
    background: #c9cdf1;
  }

  .form-inline {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
  }

  .form-inline label {
    margin: 5px 10px 5px 0;
  }

  .form-inline input {
    vertical-align: middle;
    margin: 5px 10px 5px 0;
    padding: 10px;
    background-color: #fff;
    border: 1px solid #ddd;
  }

  .form-inline button {
    padding: 10px 20px;
    background-color: dodgerblue;
    border: 1px solid #ddd;
    color: white;
  }

  .form-inline button:hover {
    background-color: royalblue;
  }

</style>