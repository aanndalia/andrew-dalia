vector < int > nge(vector < int > arr) {
    //vector<int> result(arr.size());
    vector<int> result;
    map<int, int> numMap;
    map<int, int>::iterator it;
    for(int i=0; i < arr.size(); i++){
        numMap.insert(pair<int, int>(arr[i], i));
        //cout << "arri" << arr[i] << endl;
    }
    for(int i=0; i < arr.size(); i++){ 
        it = numMap.find(arr[i]);
        it++;
        bool foundGreater = false;
        for(; it != numMap.end(); it++){
            if(it->second > i){
                //cout << "greater " << it->first << " " << it->second << endl;
                result.push_back(it->first);
                foundGreater = true;
                break;
            }
        }
        if(!foundGreater)
            result.push_back(-1);
    }
    
    return result;
}
