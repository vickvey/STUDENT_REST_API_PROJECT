import React from 'react';
import StudentList from './components/StudentList';
import AddStudent from './components/AddStudent';

function App() {
  return (
    <div className="App">
      <AddStudent />
      <StudentList />
    </div>
  );
}

export default App;
