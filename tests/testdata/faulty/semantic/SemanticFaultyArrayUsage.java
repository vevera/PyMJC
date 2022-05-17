class A {
    public static void main(String[] args){
		System.out.println(new B().oneMethod());
    }
}

class B {

    public int oneMethod(){
      int[] aux1;
      int aux2;
      int[] aux3;
      boolean value;
      int a;
       
      value = true;
      aux1 = new int[3];
      aux1[0] = value;

      //aux1[value];
      //aux2[0];
      //aux2.length;
      a = aux1[value];
      a = aux2[0];
      a = aux2.length;
      aux3 = new int[value];

		  return 0 ;
    }

}