#!/usr/bin/env python3

import unet
from submission import *
from preprocessor import *
import os
from keras import optimizers
from keras.callbacks import ModelCheckpoint

def predict(x_test, offset=0.0):
	return x_test_final

def main():

	x_train, y_train, x_val, y_val = prepare_training_data('./train/images/', './train/masks/')

	model_unet = unet.unet_model()
	adam = optimizers.Adam(lr = 1e-4)   # best run 1e-4 // defaul: 1e-3
	model_unet.compile(loss = 'binary_crossentropy', optimizer=adam, metrics=['accuracy'])

#	model.summary() # Model summary

	x_test = prepare_test_data('./test/')

	##### Run model
	filepath = 'weights.best.hdf5'
	checkpoint = ModelCheckpoint(filepath, 
		monitor='val_acc', 
		verbose=1, 
		save_best_only=True, 
		mode='max')
	callbacks_list = [checkpoint]
	model_unet.fit(x_train, y_train, 
		epochs=2, 
		batch_size=64, 
		validation_data=(x_val,y_val), 
		callbacks=callbacks_list, 
		verbose=1)


	model.load_weights('weights.best.hdf5')

	print('Predictions for validation images')
	##### Predict validations results
	y_train_pred = model_unet.predict(x_train, verbose=1)
	y_val_pred = model_unet.predict(x_val, verbose=1)


	print('Predictions for validation images')
	##### Predict validations results
	x_test_pred = model_unet.predict(x_test, verbose=1)
	x_test_final = np.round(x_test_pred[:,:,:,0]+ 0.0)


	##### Create a submission file	
	submission_file_creator(x_test_final, test_images_path)

if __name__ == '__main__':
	main()