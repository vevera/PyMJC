class A {
    public static void main(String[] args){
        System.out.println(new B().oneMethod(20));
    }
}

class B {

    public int oneMethod(int param){
        int obj;
        int a;
        
        //obj.oneMethod(20);
        a = obj.oneMethod(20);
		return param ;
    }

}