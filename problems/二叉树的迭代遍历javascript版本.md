//前序遍历
```javascript
var preorderTraversal = function(root) {
 //迭代版本的先序遍历
 let result=[];
 let stack=[];
 if(root===null){
     return result;
 }
    stack.push(root);
    while(stack.length){
        let node =stack.pop();
        result.push(node.val);
        node.right&&stack.push(node.right);
        node.left&&stack.push(node.left);
    }
    return result;
};
```
//中序遍历
```javascript
var inorderTraversal = function(root) {
    let stack=[];
    let cur=root;
    let res=[];
    if(root===null){
        return res;
    }
    while(cur!==null||stack.length!==0){
        if(cur!==null){
            stack.push(cur);
            cur=cur.left;
        }else{
            cur=stack.pop();
            res.push(cur.val);
            cur=cur.right;
        }
    }
    return res;
};
```
//后序遍历
```javascript
var postorderTraversal = function(root) {
    let res=[];
    const dfs=function(root){
        if(root===null){
            return ;
        }
        dfs(root.left);
        dfs(root.right);
        res.push(root.val);
    }
    dfs(root);
    return res;
};
```
