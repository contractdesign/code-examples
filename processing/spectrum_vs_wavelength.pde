
void setup() {
  int[] range = new int[2];
  range[0] = 380;
  range[1] = 780;

  //size( range[1] - range[0], 50 );
  size(400, 50);
  rectMode( CORNER );

  for( int wl = range[0]; wl <= range[1]; wl++ ) {
    noStroke();
    fillWL( wl );
    rect( wl - range[0], 0, 1, height/2 );
    
    stroke( 0, 0, 0 );
    if( (wl % 100) == 0 ) {
      line( wl - range[0], height/2, wl - range[0], height );
      stroke( 0, 0, 0 );
      fill(0, 0, 0);
      text( wl + "nm", wl - range[0] + 5, height*0.75);
      
    }

  }
  noLoop();
  saveFrame("spectrum.png");
    

}






void fillWL( float wl ) {
  float[] temp = lambdaColor(wl);
  fill( temp[0], temp[1], temp[2] );
}

/*

 returns color triplet as a function of wavelength (wl, units of [nm]).
 valid for wl between 380 - 780 nm
 
 based on Fortran code from: http://www.physics.sfasu.edu/astro/color/spectra.html
 
 */
float[] lambdaColor( float wl ) {
  float r = 0, g = 0, b = 0;
  float sss;
  float gamma = 1.0;
  float MAX = 255;

  if( wl < 380 || wl > 780 )
    return null;

  if( wl >= 380 && wl <= 440 ) {
    r = -(wl - 440) / (440 - 380);
    g = 0;
    b = 1;
  }
  if( wl >= 440 && wl <= 490 ) {
    r = 0;
    g = (wl - 440)/(490 - 440);
    b = 1; 
  }
  if( wl >= 490 && wl <= 510 ) {
    r = 0;
    g = 1;
    b = -(wl - 510)/(580 - 520); 
  }
  if( wl >= 510 && wl <= 580 ) {
    r = (wl - 510)/(580 - 510);
    g = 1;
    b = 0; 
  }
  if( wl >= 580 && wl <= 645 ) {
    r = 1;
    g = -(wl - 645)/(645 - 580);
    b = 0; 
  }
  if( wl >= 645 && wl <= 780 ) {
    r = 1;
    g = 0;
    b = 0; 
  }

  if( wl > 700 )
    sss = 0.3 + 0.7 * (780 - wl)/(780 - 700 );
  else if( wl < 420 )
    sss = 0.3 + 0.7* (wl - 380)/(420 - 380);
  else
    sss = 1;

  float[] temp = new float[3];
  temp[0] = pow( MAX*sss*r, gamma );
  temp[1] = pow( MAX*sss*g, gamma );
  temp[2] = pow( MAX*sss*b, gamma );

  return temp;
}
